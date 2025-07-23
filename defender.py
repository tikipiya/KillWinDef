import subprocess

def disable_windows_defender():
    try:
        # Windows Defenderのリアルタイム保護を無効化
        subprocess.run(['powershell', '-Command', 'Set-MpPreference -DisableRealtimeMonitoring $true'], check=True)
        print("Windows Defenderのリアルタイム保護が無効化されました。")
    except subprocess.CalledProcessError as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    disable_windows_defender()