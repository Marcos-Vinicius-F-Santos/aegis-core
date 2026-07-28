import os
import sys
import uvicorn

def main():
    # Set working directory to aegis/services/vex
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vex_dir = os.path.join(base_dir, "aegis", "services", "vex")
    
    if not os.path.exists(vex_dir):
        print(f"[ERROR] Vex service directory not found at: {vex_dir}")
        sys.exit(1)
        
    sys.path.insert(0, vex_dir)
    os.chdir(vex_dir)
    
    print("========================================================")
    print("             Aegis-Core Local AI Server                 ")
    print("========================================================")
    print("Servidor rodando em: http://localhost:8000")
    print("Interface Web:      http://localhost:8000/")
    print("Documentacao API:   http://localhost:8000/docs")
    print("========================================================\n")
    
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
