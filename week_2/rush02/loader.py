import sys
import csv
import json
from pathlib import Path
from sqlalchemy import create_engine, Column, Float, Text
from sqlalchemy.orm import sessionmaker, declarative_base

def clean_fieldnames(fieldnames):
    return [fn.strip().lstrip('\ufeff') if fn else fn for fn in fieldnames]

def read_csv(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        first_line = f.readline()
        if not first_line:
            return []
        f.seek(0)
        reader = csv.DictReader(f)
        if reader.fieldnames:
            reader.fieldnames = clean_fieldnames(reader.fieldnames)
        dados = list(reader)
    return dados

def coerce_and_clean(dados):
    cleaned = {}
    for row in dados:
        numero = row.get('numero') or row.get('numero '.strip()) or row.get(' account_number') or ''
        numero = (numero or '').strip()
        if not numero:
            continue
        if numero in cleaned:
            continue
        titular = (row.get('titular') or '').strip()
        def to_float(v):
            if v is None or str(v).strip() == '':
                return 0.0
            try:
                return float(str(v).strip())
            except Exception:
                raise ValueError(f"Valor inválido numérico: {v} (conta {numero})")
        saldo = to_float(row.get('saldo'))
        limite = to_float(row.get('limite'))
        data_abertura = str(row.get('data_abertura') or '').strip()
        cleaned[numero] = {
            'numero': numero,
            'titular': titular,
            'saldo': saldo,
            'limite': limite,
            'data_abertura': data_abertura
        }
    return list(cleaned.values())

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 loader.py <source.csv|.jsonl> [database.db] [--recreate]")
        sys.exit(1)

    source = sys.argv[1]
    db_file = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else 'meu_banco.db'
    recreate = '--recreate' in sys.argv

    dados = []
    try:
        if source.endswith('.csv'):
            raw = read_csv(source)
            dados = coerce_and_clean(raw)
        elif source.endswith('.jsonl'):
            with open(source, 'r', encoding='utf-8') as f:
                raw = [json.loads(line) for line in f if line.strip()]
            dados = coerce_and_clean(raw)
        else:
            print("Error: file not supported")
            sys.exit(1)
    except Exception as e:
        print("Error reading/converting file:", e)
        sys.exit(1)

    engine = create_engine(f"sqlite:///{db_file}")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class Accounts(Base):
        __tablename__ = 'accounts'
        numero = Column(Text, primary_key=True)
        titular = Column(Text, nullable=False)
        saldo = Column(Float, default=0.0)
        limite = Column(Float, default=0.0)
        data_abertura = Column(Text, nullable=False)

    if recreate:
        print("Recriando tabela 'accounts' (DROP + CREATE).")
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    import pprint
    print("Prontos para inserir (20 primeiros):")
    pprint.pprint(dados[:20])

    try:
        session.bulk_insert_mappings(Accounts, dados)
        session.commit()
        print("Inserção concluída.")
    except Exception as e:
        session.rollback()
        print("Erro ao inserir no banco:", e)
        print("Verifique o schema da tabela e tipos. Para inspecionar externamente use:")
        print(f"  sqlite3 {db_file} \"PRAGMA table_info(accounts);\"")
        raise
    finally:
        session.close()
