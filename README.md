# Crypto API Testing 💻📈 *beta*

<img width="361" height="271.5" alt="Screenshot 2026-01-18 123122" src="https://github.com/user-attachments/assets/3602e9ef-7345-41a6-abf0-9811dde8bd76" />

A lightweight sandbox for testing and comparing **Binance**, **OKX**, and **Bybit** APIs.  
This project focuses on fetching real‑time and historical crypto market data using both REST and WebSocket endpoints.

Useful for:
- Traders exploring exchange data differences   
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

### **Binance (SOON)**
- REST + WebSocket  
- Spot + Futures  
- Fast responses, good documentation  
- Some endpoints require API keys  

### **OKX (SOON)**
- REST + WebSocket  
- Spot + Futures + Options  
- Very structured API  
- Most endpoints require signing  

### **Bybit (WEBSOCKET DONE)**
- REST + WebSocket  
- Spot + USDT/USDC Perps  
- Clean endpoints  
- Occasional rate‑limit quirks  

---
## 📁 Project Structure

Available Soon

---

## 🧪 What I am Testing

### **Market Data**
- Orderbook snapshots  
- Live orderbook streams  
- Trades (tick‑by‑tick)  
- Candles (1s → 1M)  

### **Derivatives Data**
- Funding rates  
- Open interest  
- Mark price  
- Index price  

### **Performance**
- REST latency  
- WebSocket stability  
- Rate‑limit behavior  
- Data consistency across exchanges  

---

📝 Notes
This repo is for learning and testing, not production trading.

Follow exchange rate limits.

WebSocket connections may require reconnection logic.
