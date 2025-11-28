from agent import LlmAgent

if __name__ == "__main__":
  agent = LlmAgent()
  reply = agent.handle("사용자", "안녕")
  print("응답:", reply)