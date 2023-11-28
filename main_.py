import tkinter as tk
from tkinter import messagebox
import winreg
import random
import string

hosts = """
127.0.0.1           tonec.com
127.0.0.1           www.tonec.com
127.0.0.1           registeridm.com
127.0.0.1           www.registeridm.com
127.0.0.1           secure.registeridm.com
127.0.0.1           internetdownloadmanager.com
127.0.0.1           www.internetdownloadmanager.com
127.0.0.1           secure.internetdownloadmanager.com
127.0.0.1           mirror.internetdownloadmanager.com
127.0.0.1           mirror2.internetdownloadmanager.com
127.0.0.1           mirror3.internetdownloadmanager.com
"""
def delete_key(hkey, path):
    try:
        key = winreg.OpenKey(hkey, path)
        winreg.DeleteKey(key, "")
        print(f"Successfully deleted {path}")
    except FileNotFoundError:
        print(f"{path} does not exist")
    except PermissionError:
        print(f"No permission to delete {path}")

def delete_value(hkey, key_path, value_name):
    try:
        key = winreg.OpenKey(hkey, key_path, access=winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, value_name)
        print(f"Successfully deleted {value_name} from {key_path}")
    except FileNotFoundError:
        print(f"{key_path} does not exist")
    except OSError:
        print(f"{value_name} does not exist in {key_path}")

def set_value(hkey, key_path, value_name, value_data):
    try:
        key = winreg.OpenKey(hkey, key_path, access=winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        print(f"Successfully set {value_name} to {value_data} in {key_path}")
    except FileNotFoundError:
        print(f"{key_path} does not exist")

def add_value(hkey, key_path, value_name, value_data):
    try:
        key = winreg.CreateKey(hkey, key_path)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_BINARY, value_data)
        print(f"Successfully added {value_name} to {key_path}")
    except FileNotFoundError:
        print(f"{key_path} does not exist")

def generate_key():
    parts = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for _ in range(4)]
    return '-'.join(parts)

def execute_operations():
    fname = fname_entry.get()
    lname = lname_entry.get()
    serial = serial_entry.get()
    if not fname or not lname:
        error_label.config(text="Please add first name or last name")
        return

    if not serial:
        error_label.config(text="Please generate a key first")
        return
    # Delete keys
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}")
    delete_key(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}")
    delete_key(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}")
    
    # Delete values
    delete_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "FName")
    delete_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "LName")
    delete_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Email")
    delete_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Serial")
#    delete_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Serial")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "FName")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "LName")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "Email")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "Serial")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Internet Download Manager", "FName")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Internet Download Manager", "LName")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Internet Download Manager", "Email")
    delete_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Internet Download Manager", "Serial")


    # Set values
    #for 32bit
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "FName", fname)
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "InstallStatus", "dword:00000003" )
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "LName", lname)
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Email", "mina")
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Serial", serial)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\DownloadManager", "FName", fname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\DownloadManager", "InstallStatus", "dword:00000003" )
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\DownloadManager", "LName", lname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\DownloadManager", "Serial", serial)
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "Email", "mina")

    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "TipStartUp", "dword:00000001")
    set_value(winreg.HKEY_CURRENT_USER, r"Software\DownloadManager", "LstCheck", "1/1/99")

    
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "FName", fname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "InstallStatus", "dword:00000003" )
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "LName", lname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "Serial", serial)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager", "Serial", serial)
    #for 64bit
    set_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Internet Download Manager", "FName", fname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Internet Download Manager", "InstallStatus", "dword:00000003")
    set_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Internet Download Manager", "LName", lname)
    set_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Internet Download Manager", "Email", "SPYOPS@gmail.com")
    set_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Internet Download Manager", "Serial", serial)

    # Add binary values
    scansk_data = bytes.fromhex('6f4e79b5cc8b50bbf4b7e26d2e38d28bad100b03a61b53306bb88b92d60422c755b9a5334da84e9b0000000000000000')
    
    add_value(winreg.HKEY_CURRENT_USER,r"Software\DownloadManager","scansk",scansk_data)
    
    add_value(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}","scansk",scansk_data)
    
    add_value(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}","scansk",scansk_data)
    
    add_value(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}","scansk",scansk_data)
    
    add_value(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}","scansk",scansk_data)

    # Add MData values
    mdata_data = bytes.fromhex('219eac77b5b5263c9dff86402db9556c1317812f93542eab2c34cadc321fa4b0c6cc4c8348842c1e685f4dd7ac412e525c6a4a787c3b398db3d562d6a0e812e5468f3cf25c68ee2115a40a99abbfd82c5c773b0133e99b4f128ec4a7a1359feb15a40a99abbfd82cefac0dee9b62b8891c4298d236ceb39ee756885bcc7f1d4034a2cd43fee6971540116c233f1a3c920bf920e617ac22688f453016840df4de9ce8e5a9155dd91c22d21b762db4c4bbe88471b7168a2e35a0a86649b71aec380b5f4e354e593163cdd2af854e9032ea154453e08d7baf34b8fec8ec2cef8a260177385bdf31596536d851ef7f206d43d6c2e8d6171816a4d0f3eaf783c55500')

    add_value(winreg.HKEY_CURRENT_USER,r"Software\Classes\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}","MData",mdata_data)
    
    add_value(winreg.HKEY_CURRENT_USER,r"Software\Classes\Wow6432Node\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}","MData",mdata_data)
    
    add_value(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}","MData",mdata_data)
    
    add_value(winreg.HKEY_LOCAL_MACHINE,r"Software\Classes\Wow6432Node\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}","MData",mdata_data)
    try:
        with open("C:\\Windows\\System32\\Drivers\\etc\\hosts", "a") as file:
            file.write(hosts)
        messagebox.showinfo("Success", "IDM Patched successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def help_button_clicked():
    messagebox.showinfo("Help", "This program is an IDM Patcher. It allows you to set up IDM (Internet Download Manager) by providing a first name, last name, and generating a serial key. You can click on the 'Generate Serial' button to create a serial key and then use the 'Execute Operations' button to apply changes. For more information, visit:\n\nLink 1: www.example1.com\nLink 2: www.example2.com")

def about_button_clicked():
    messagebox.showinfo("About", "IDM Patcher\nVersion: 1.0\n\nThis program helps in configuring Internet Download Manager (IDM) by setting up necessary keys and values in the system registry. It provides a convenient way to manage IDM settings easily. For more details and updates, visit:\n\nLink 3: www.example3.com")

def generate_and_set_serial():
    serial = generate_key()
    serial_entry.delete(0, tk.END)
    serial_entry.insert(0, serial)

root = tk.Tk()
root.geometry("430x240")
root.resizable(False, False)
root.attributes('-topmost', 1)
root.title("IDMPatcher")
root.configure(bg="#064789") 


btn_bg_color = "#427aa1"
btn_bgg_color = "#064789"
btn_txt_color = "#ebf2fa"
label_fg_color = "#ebf2fa"

font_label = ("Arial", 11)
font_button = ("Arial", 10)


fname_label = tk.Label(root, text="I D M   P a t c h e r   P R O  [ I D M P P ]\nDev.m.malaak", fg=label_fg_color, bg="#064789", font=("Arial", 11, "bold"))
fname_label.grid(row=0, column=1)

fname_label = tk.Label(root, text="First Name", fg=label_fg_color, bg="#064789", font=font_label)
fname_label.grid(row=1, column=0)
fname_entry = tk.Entry(root, width=30, bd=0, bg="#ebf2fa", font=font_label)
fname_entry.grid(row=1, column=1)

lname_label = tk.Label(root, text="Last Name", fg=label_fg_color, bg="#064789", font=font_label)
lname_label.grid(row=2, column=0)
lname_entry = tk.Entry(root, width=30, bd=0, bg="#ebf2fa", font=font_label)
lname_entry.grid(row=2, column=1)

serial_label = tk.Label(root, text="Serial", fg=label_fg_color, bg="#064789", font=font_label)
serial_label.grid(row=3, column=0)
serial_entry = tk.Entry(root, width=30, bd=0, bg="#ebf2fa", font=font_label)
serial_entry.grid(row=3, column=1)

generate_button = tk.Button(root, text="Generate Serial", command=generate_and_set_serial, bd=0, bg=btn_bg_color, activebackground=btn_bgg_color, fg=btn_txt_color, font=font_button, width=30, height=1)
generate_button.grid(row=4, column=1, pady=10)

generated_key_label = tk.Label(root, text="", fg=label_fg_color, bg="#064789", font=font_label)
generated_key_label.grid(row=5, column=0)

execute_button = tk.Button(root, text="Execute Operations", command=lambda: execute_operations(), bd=0, bg=btn_bg_color, activebackground=btn_bgg_color, fg=btn_txt_color, font=font_button, width=30, height=1)
execute_button.grid(row=5, column=1, pady=10)
error_label = tk.Label(root, text="", fg="red", bg="#064789", font=font_label)
error_label.grid(row=8, column=0, columnspan=2)

help_button = tk.Button(root, text="Help", command=help_button_clicked, bd=0, bg=btn_bg_color, activebackground=btn_bgg_color, fg=btn_txt_color, font=font_button, width=5, height=2)
help_button.place(x=360,y=50)

about_button = tk.Button(root, text="About", command=about_button_clicked, bd=0, bg=btn_bg_color, activebackground=btn_bgg_color, fg=btn_txt_color, font=font_button, width=5, height=2)
about_button.place(x=360,y=100)


root.mainloop()


