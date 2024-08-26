import subprocess
import os

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError:
        print(f"Failed to execute command: {command}")

def main():
    # Update and clean system packages
    commands = [
        "sudo apt clean", "sudo apt autoclean", "sudo apt autoremove -y",
        "sudo apt update", "sudo apt --fix-broken install", "sudo apt clean",
        "sudo apt list --upgradable", "sudo apt full-upgrade -y",
        "sudo apt install zsh curl git -y",
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',
        "sudo apt install fonts-firacode -y"
    ]

    # Execute all setup and installation commands
    for command in commands:
        run_command(command)
    
    # Set Zsh as the default shell
    zsh_path = subprocess.check_output("which zsh", shell=True).decode().strip()
    run_command(f"chsh -s {zsh_path}")
    
    # Install Powerlevel10k theme and Zinit
    run_command("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k")
    run_command('bash -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"')
    
    # Configure .zshrc to use Powerlevel10k and Zinit plugins
    config_lines = [
        "source ~/powerlevel10k/powerlevel10k.zsh-theme",
        "zinit light zdharma-continuum/fast-syntax-highlighting",
        "zinit light zsh-users/zsh-autosuggestions",
        "zinit light zsh-users/zsh-completions"
    ]
    
    with open(os.path.expanduser("~/.zshrc"), "a") as f:
        for line in config_lines:
            f.write(f"{line}\n")
    
    print("Installation and configuration complete. Please logout and login again for the changes to take effect.")

if __name__ == "__main__":
    main()
