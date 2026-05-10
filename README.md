# crypto-api-testing

A lightweight sandbox for testing and comparing **Binance**, **OKX**, and **Bybit** APIs.  
This project focuses on fetching real‑time and historical crypto market data using both REST and WebSocket endpoints.

Useful for:
- Traders exploring exchange data differences  
- Quant researchers  
- Bot developers  
- Anyone learning exchange APIs  

---

## 🚀 Purpose

This repository provides a unified environment to test:

- Orderbook (L2) snapshots and streams  
- Trades (tick data)  
- Klines / candles  
- Funding rates  
- Open interest  
- Mark/index prices  
- REST vs WebSocket latency  
- Exchange data structure differences  

This is **not** a trading bot — it’s purely for API exploration and benchmarking.

---

## 📦 Supported Exchanges

### **Binance**
- REST + WebSocket  
- Spot + Futures  
- Fast responses, good documentation  
- Some endpoints require API keys  

### **OKX**
- REST + WebSocket  
- Spot + Futures + Options  
- Very structured API  
- Most endpoints require signing  

### **Bybit**
- REST + WebSocket  
- Spot + USDT/USDC Perps  
- Clean endpoints  
- Occasional rate‑limit quirks  

---

## 📁 Project Structure

