from orchestrator.orchestrator import LucyOrchestrator

def main():
    lucy = LucyOrchestrator()
    lucy.initialize()
    
    # Print health status of all agents
    report = lucy.health_report()
    for agent_name, status in report.items():
        print(f"{agent_name}: {status}")
    
    # Run Lucy (placeholder for main loop or CLI)
    lucy.run()
    
    # Shutdown when done
    lucy.shutdown()

if __name__ == "__main__":
    main()
