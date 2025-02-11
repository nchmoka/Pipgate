import sys
from core.security import audit_package
from core.package_manager import install_package

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'install':
        print('Usage: pipgate install <package>')
        sys.exit(1)

    package = sys.argv[2]
    print(f'🔍 Auditing package: {package}...')

    is_safe, reason = audit_package(package)
    if not is_safe:
        print(f'❌ Installation blocked: {reason}')
        sys.exit(1)

    print(f'✅ {package} passed security checks. Installing...')
    install_package(package)

if __name__ == '__main__':
    main()