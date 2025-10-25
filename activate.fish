#!/bin/bash
# Script de activación del entorno virtual para fish shell

echo "🐍 Activando entorno virtual de Python..."
source venv/bin/activate.fish

echo "✅ Entorno virtual activado"
echo ""
echo "📦 Versiones instaladas:"
python -c "import pandas as pd; import numpy as np; import matplotlib; import seaborn as sns; print(f'  - Pandas: {pd.__version__}'); print(f'  - NumPy: {np.__version__}'); print(f'  - Matplotlib: {matplotlib.__version__}'); print(f'  - Seaborn: {sns.__version__}')"
echo ""
echo "💡 Para desactivar el entorno, ejecuta: deactivate"
echo ""
