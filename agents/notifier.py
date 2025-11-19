def send_alert(recommendations_df):
    if recommendations_df.empty:
        print("✅ No actions required today.")
    else:
        print("\n===== ACTION ALERTS =====")
        print(recommendations_df.to_string(index=False))
        print("=========================\n")
