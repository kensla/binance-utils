#!/usr/bin/env python3
import json

from binance_utils import get_exchange_info


print(json.dumps(get_exchange_info()))
