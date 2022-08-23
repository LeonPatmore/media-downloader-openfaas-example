import sys
from unittest.mock import MagicMock

configuration_mock = MagicMock()


sys.modules['configuration'] = configuration_mock
