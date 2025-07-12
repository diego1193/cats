#!/usr/bin/env python3
"""
Setup script for Cat Breeds & Users API
"""
import os
import sys
import subprocess


def create_venv():
    """Create virtual environment"""
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("Virtual environment created successfully!")


def install_dependencies():
    """Install project dependencies"""
    print("Installing dependencies...")
    pip_cmd = ["venv/Scripts/pip", "install", "-r", "requirements.txt"]
    if os.name != 'nt':  # Unix/Linux
        pip_cmd = ["venv/bin/pip", "install", "-r", "requirements.txt"]
    
    subprocess.run(pip_cmd, check=True)
    print("Dependencies installed successfully!")


def main():
    """Main setup function"""
    try:
        create_venv()
        install_dependencies()
        print("\nSetup completed successfully!")
        print("To activate the virtual environment:")
        if os.name == 'nt':
            print("  .\\venv\\Scripts\\activate")
        else:
            print("  source venv/bin/activate")
        print("\nTo run the application:")
        print("  python main.py")
        print("\nTo run tests:")
        print("  pytest")
        
    except subprocess.CalledProcessError as e:
        print(f"Setup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 