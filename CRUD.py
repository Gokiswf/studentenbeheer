import Database as db
from PIL import Image

def ToonStudenten():
    connectie = db.maakConnectie()
    if connectie is None:
        return None
    cur = connectie.cursor()
    cur.execute('SELECT * FROM studentengegevens')
    rows = cur.fetchall()
    db.sluitConnectie()
    return rows

def BewaarStudent(naam: str, leeftijd: str, email: str, opleiding: str):
    connectie = db.maakConnectie()
    if connectie is None:
        return None
    
    cur = connectie.cursor()
    waarden = """INSERT INTO studentengegevens (naam, leeftijd, email, opleiding) 
               VALUES (%s, %s, %s, %s)"""
    
    values = (naam, leeftijd, email, opleiding)
    
    cur.execute(waarden, values)
    connectie.commit()
    db.sluitConnectie()
    
    return cur.rowcount

def VerwijderStudent(id):
    connectie = db.maakConnectie()
    if connectie is None:
        return None
    
    cur = connectie.cursor()
    try:
        cur.execute("DELETE FROM studentengegevens WHERE id = %s", (id,))
        connectie.commit()
        return cur.rowcount
    except Exception as e:
        print(f"Fout bij het verwijderen van student: {e}")
        return 0
    finally:
        db.sluitConnectie()

def WijzigStudent(id: int, naam: str, leeftijd: str, email: str, opleiding: str):
    connectie = db.maakConnectie()
    if connectie is None:
        return None
    
    try:
        cur = connectie.cursor()
        query = """UPDATE studentengegevens
                   SET 
                   naam = %s,
                   leeftijd = %s,
                   email = %s,
                   opleiding = %s
                   WHERE id = %s"""
        
        values = (naam, leeftijd, email, opleiding, id)
        
        cur.execute(query, values)
        connectie.commit()
        return cur.rowcount 
    
    except Exception as e:
        print(f"Fout bij het bijwerken van student: {e}")
        return 0 
    
    finally:
        db.sluitConnectie()