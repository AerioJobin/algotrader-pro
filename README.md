# algotrader-pro

A professional-grade **Algorithmic Trading Backtesting Platform** built with FastAPI, TimescaleDB, and Redis. Designed for quantitative traders and financial engineers to develop, test, and optimize trading strategies at scale.

## Overview

algotrader-pro provides a robust, production-ready backtesting engine with real-time market data simulation, advanced order handling, and comprehensive performance analytics. Built specifically for traders who need institutional-grade accuracy and performance.

## Key Features

- **Advanced Backtesting Engine**: Multi-asset, multi-timeframe backtesting with realistic market microstructure
- **FastAPI Backend**: High-performance REST API for strategy submission and results retrieval
- **TimescaleDB Integration**: Time-series optimized database for efficient OHLCV data storage and queries
- **Redis Caching**: Real-time data caching and queue management for strategy execution
- **Risk Analytics**: Sharpe ratio, Sortino ratio, maximum drawdown, win rate, and more
- **Performance Metrics**: Detailed trade-by-trade analysis with entry/exit signals
- **Portfolio Simulation**: Multi-strategy portfolio backtesting with correlation analysis
- **Web Dashboard**: Interactive UI for strategy visualization and results exploration

## Tech Stack

```
Backend:        FastAPI, Python 3.10+
Database:       PostgreSQL + TimescaleDB extension
Cache:          Redis
ORM:            SQLAlchemy
Data Handling:  Pandas, NumPy
Visualization:  Plotly, Matplotlib
Testing:        Pytest, Docker
```

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL 12+
- Redis 6.0+
- Docker & Docker Compose (optional, for containerized setup)

### Quick Start

```bash
# Clone repository
git clone https://github.com/AerioJobin/algotrader-pro.git
cd algotrader-pro

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your database and Redis credentials

# Initialize database
alembic upgrade head

# Start FastAPI server
uvicorn app.main:app --reload
```

### Docker Compose Setup

```bash
docker-compose up -d
# Application available at http://localhost:8000
```

## Usage

### Running a Backtest

```python
from algotrader.backtester import Backtester
from algotrader.strategy import Strategy

class MyStrategy(Strategy):
    def __init__(self):
        self.position_size = 0.1
    
    def on_bar(self, data):
        if data['close'] > data['sma_20']:
            self.buy()
        elif data['close'] < data['sma_20']:
            self.sell()

backtester = Backtester(
    strategy=MyStrategy(),
    symbol='BTC/USD',
    start_date='2023-01-01',
    end_date='2024-01-01',
    initial_capital=100000
)

results = backtester.run()
print(results.performance_summary())
```

### API Endpoints

```
POST   /api/v1/backtest          - Submit new backtest
GET    /api/v1/backtest/{id}     - Get backtest results
GET    /api/v1/backtest/{id}/trades - Get detailed trade log
GET    /api/v1/symbols           - List available symbols
GET    /api/v1/data/{symbol}     - Retrieve OHLCV data
```

## Project Structure

```
algotrader-pro/
├── app/
│   ├── main.py              # FastAPI application
│   ├── api/                 # API route handlers
│   ├── models/              # Database models
│   ├── schemas/             # Pydantic schemas
│   └── services/            # Business logic
├── algotrader/
│   ├── backtester.py        # Core backtesting engine
│   ├── strategy.py          # Base strategy class
│   ├── indicators.py        # Technical indicators
│   └── analytics.py         # Performance metrics
├── tests/                   # Unit and integration tests
├── docker-compose.yml       # Container orchestration
├── requirements.txt         # Python dependencies
└── README.md
```

## Performance Metrics

The backtester calculates comprehensive performance metrics:

- **Sharpe Ratio**: Risk-adjusted return metric
- **Sortino Ratio**: Downside risk-adjusted return
- **Maximum Drawdown**: Largest peak-to-trough decline
- **Win Rate**: Percentage of profitable trades
- **Profit Factor**: Gross profit / Gross loss
- **Calmar Ratio**: Return over maximum drawdown
- **CAGR**: Compound annual growth rate

## Configuration

Edit `.env` to customize:

```env
DATABASE_URL=postgresql://user:password@localhost/algotrader
REDIS_URL=redis://localhost:6379
API_KEY=your-secret-key
MAX_WORKERS=4
```

## Development

```bash
# Run tests
pytest tests/ -v

# Code formatting
black .

# Linting
flake8 app/ algotrader/

# Type checking
mypy app/
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Machine learning strategy optimization
- [ ] Real-time paper trading integration
- [ ] Multi-exchange support (Binance, Kraken, etc.)
- [ ] Advanced portfolio optimization (mean-variance, risk parity)
- [ ] Sentiment analysis integration
- [ ] Mobile app for monitoring backtests

## License

MIT License - See LICENSE file for details

## Contact & Support

For questions, issues, or feedback:

- **GitHub Issues**: [Report a bug or request feature](https://github.com/AerioJobin/algotrader-pro/issues)
- **LinkedIn**: [in/aeriojobinmomin](https://linkedin.com/in/aeriojobinmomin)
- **Email**: aeriojobin@gmail.com

---

**Created by**: AerioJobin | **Last Updated**: Feb 4, 2026
