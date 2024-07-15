


import winreg as reg

def disable_system_sounds():
    registry_path = r"AppEvents\Schemes\Apps\.Default"
    sound_events = [
        ".Default",
        "SystemAsterisk",
        "SystemExclamation",
        "SystemExit",
        "SystemHand",
        "SystemQuestion",
        "SystemStart"
    ]
    
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE)
        for sound_event in sound_events:
            event_key_path = f"{sound_event}\\.Current"
            try:
                event_key = reg.OpenKey(key, event_key_path, 0, reg.KEY_SET_VALUE)
                reg.SetValueEx(event_key, "", 0, reg.REG_SZ, "")
                reg.CloseKey(event_key)
            except FileNotFoundError:
                print(f"Sound event '{sound_event}' not found in the registry.")
        
        reg.CloseKey(key)
        print("System sounds disabled successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    disable_system_sounds()


