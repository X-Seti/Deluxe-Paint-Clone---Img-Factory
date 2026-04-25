#!/usr/bin/env python3
#this belongs in root /launch_dp5_workshop.py - Version: 1
# X-Seti - April25 2026 - DP5 Workshop - Root Launcher

import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    try:
        print("DP5 Workshop Starting...")
        from PyQt6.QtWidgets import QApplication
        from apps.components.DP5_Workshop.dp5_workshop import DP5Workshop
        app = QApplication(sys.argv)
        workshop = DP5Workshop()
        workshop.show()
        sys.exit(app.exec())
    except ImportError as e:
        print(f"ERROR: Failed to import dp5_workshop: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to start DP5 Workshop: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
