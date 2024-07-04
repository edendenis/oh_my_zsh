# Como configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos para configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands for configuring/installing/use `oh-my-zsh` on `Linux Ubuntu`._

## Descrição [2]

### `shell`

Um `shell` é uma interface de linha de comando que permite aos usuários interagirem com um sistema operacional por meio de comandos de texto. Ele interpreta os comandos inseridos pelo usuário e os executa, facilitando a manipulação de arquivos, a execução de programas e outras tarefas do sistema. Além disso, os shells também oferecem recursos avançados, como redirecionamento de entrada e saída, expansão de comandos e controle de processos. Exemplos comuns incluem o Bash, o `Zsh` e o `PowerShell`.

### `bash`

`Bash`, ou `Bourne Again Shell`, é um `shell` de linha de comando amplamente utilizado em sistemas operacionais Unix e `Linux`. Ele oferece uma variedade de recursos, como expansão de comandos, redirecionamento de entrada/saída, scripts de `shell` e controle de processos. O Bash é altamente personalizável e suporta automação de tarefas por meio de scripts, tornando-o uma ferramenta poderosa para usuários avançados e administradores de sistemas. Sua sintaxe simples e intuitiva o torna acessível para iniciantes, enquanto sua flexibilidade e extensibilidade o tornam uma escolha popular entre profissionais de TI.

### `zsh`

O `oh-my-zsh`, ou `Z Shell`, é um interpretador de `shell` de código aberto e uma alternativa avançada ao `bash` (`Bourne Again Shell`), que é comumente usado em sistemas Unix e Linux. O `oh-my-zsh` oferece uma série de recursos avançados, como autocompletamento poderoso, histórico de comandos expandido, personalização flexível da aparência e do comportamento do `shell`, além de suporte a plugins e temas. Sua interface de linha de comando aprimorada e recursos de automação tornam-no uma escolha popular entre desenvolvedores, administradores de sistema e entusiastas de terminal que desejam uma experiência de linha de comando mais produtiva e personalizável. O `oh-my-zsh` é altamente configurável e pode ser estendido por meio de plugins, tornando-o uma ferramenta versátil para trabalhar com eficiência no ambiente Unix e Linux.

### `oh-my-zsh`

`Oh-my-zsh` é um framework de código aberto para gerenciar a configuração do shell `Zsh`, fornecendo um conjunto de plugins, temas e ferramentas para aprimorar a experiência do usuário. Ele simplifica a personalização do ambiente de linha de comando, oferecendo recursos como autocompletar, atalhos de teclado e sugestões contextuais, aumentando a produtividade e a eficiência dos usuários. Com uma comunidade ativa e uma grande variedade de extensões disponíveis, o Oh-my-zsh é amplamente utilizado por desenvolvedores e usuários avançados para customizar e otimizar o ambiente de terminal.

### `zinit`

O `Zinit` é um gerenciador de plugins e temas para o `Zsh`, projetado para simplificar e otimizar o processo de personalização do ambiente de linha de comando. Com recursos avançados de carregamento assíncrono, ele oferece uma inicialização rápida do shell, permitindo aos usuários instalar e atualizar facilmente extensões, temas e utilitários adicionais. Além disso, o `Zinit` suporta a configuração flexível de plugins, garantindo compatibilidade com diferentes workflows e necessidades de desenvolvimento. Com uma sintaxe intuitiva e uma vasta biblioteca de extensões disponíveis, o `Zinit` é uma ferramenta poderosa para aumentar a produtividade e a eficiência dos usuários do Zsh.


## 1. Como configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    

Para configurar/instalar/usar o `oh-my-zsh` em um sistema `Linux Ubuntu`, você pode seguir estes passos:

1. Primeiro, instale o `oh-my-zsh` com o comando: `sudo apt install zsh -y`

2. **Instalar os pacotes `curl` e `git`**: `sudo apt install curl git -y`


3. **Instalar o `oh-my-zsh`**: `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

4. **Instalar o `zinit`**: `bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"`

5. **Abrir o arquivo `~/.zshrc`**: `sudo nano ~/.zshrc`

6. **Editar o arquivo `~/.zshrc`**:

    ```
    # Adicionar no final do .zshrc
    zinit light zdharma-continuum/fast-syntax-highlighting
    zinit light zsh-users/zsh-autosuggestions
    zinit light zsh-users/zsh-completions
    ```

7. Fechar o `Terminal Emulator` e abrir novamente

8. **Criar diretório**: `mkdir ~/.fonts`

9. **Baixar fonte**: `wget -P ~/.fonts 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/BitstreamVeraSansMono.zip'` 

10. **Descompactar fonte**: `unzip ~/.fonts/BitstreamVeraSansMono.zip -d ~/.fonts`

11. **Instalar a fonte `firacode`**: `sudo apt install fonts-firacode -y`

12. Fechar o `Terminal Emulator` e abrir novamente

13. Clicar na aba: `Edit`

14. Clicar em `Preferences...`

15. No campo `Font` clicar na fonte e alterar para `Fira Code Regular`

16. **Instalar o tema `powerlevel10k`**:

    ```
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
    echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
    ```

17. **Abrir o arquivo `~/.zshrc`**: `sudo nano ~/.zshrc`

18. **Editar o arquivo `~/.zshrc`**: `ZSH_THEME="powerlevel10k/powerlevel10k"`

19. Fechar o `Terminal Emulator` e abrir novamente

20. Confirmar os símbos que estiver vendo para que a configuração reconheca e configure corretamente.

21. Em `Prompt Style` escolha a opção:  `(3) Rainbow.`

22. Em `Character Set` escolha a opção:  `(1) Unicode.`

23. Em `Show current time?` escolha a opção:  `(2) 24-hour format.`

24. Em `Prompt Separators` escolha a opção:  `(1) Angled.`

25. Em `Prompt Heads` escolha a opção:  `(3) Sharp.`

26. Em `Prompt Tails` escolha a opção:  `(1) Flat.`

27. Em `Prompt Height` escolha a opção:  `(2) Two lines.`

28. Em `Prompt Connection` escolha a opção:  `(3) Solid.`

29. Em `Prompt Frame` escolha a opção:  `(4) Full.`

30. Em `Connection & Frame Color` escolha a opção:  `(1) Lightest.`

31. Em `Prompt Spacing` escolha a opção:  `(2) Sparse.`

32. Em `Icons` escolha a opção:  `(2) Many icons.`

33. Em `Prompt Flow` escolha a opção:  `(1) Concise.`

34. Em `Enable Transient Prompt` escolha a opção:  `(n) No.`

35. Em `Instant Prompt Mode` escolha a opção:  `(1) Verbose (recommended).`

36. Em `Apply changes to ~/.zshrc` escolha a opção:  `(y) Yes (recommended).`

37. **Clone o repositório**: `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`

38. Execute o comando: `ls -l -- ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`


### 1.1 Configurar o `oh-my-zsh` como seu `shell` padrão

1. **Configurar o `oh-my-zsh` como seu `shell` Padrão:** Para configurar o `oh-my-zsh` como seu `shell` padrão, use (**NÃO** colocar o `sudo`!): `chsh -s $(which zsh)`

    - Você precisará fazer logout e login novamente para que a mudança tenha efeito.

2. **Criar o Arquivo .`zshrc`:** Se, por algum motivo, o arquivo `.zshrc` **NÃO** for criado automaticamente, você pode criá-lo manualmente: `sudo nano ~/.zshrc`

    - Adicione as configurações que deseja e salve o arquivo.

3. **Aplicar as alterações:** Para que as mudanças tenham efeito, você precisa recarregar o arquivo de configuração. Isso pode ser feito com o comando: `source ~/.zshrc`

    Ou simplesmente feche e reabra o terminal.

Esses passos devem ajudar a configurar o `oh-my-zsh` com o tema e os plugins desejados. Se tiver dificuldades com algum plugin específico, pode ser útil consultar a documentação do Oh My `oh-my-zsh` ou procurar ajuda específica para aquele plugin.


## 1. Ajustes

### 1.1 Ajustar as cores do `Terminal Emulator`

1. No `Terminal Emulator`, na barra de ferramentas, clicar em: `Edit`

2. Clique em: `Preferênces`

3. Clique na aba `Appearence`

    3.1 Em `Background` altere a opção para `Transparent background`

    3.2 Em `Opacity` coloque em `0.85`

4. Clique na aba `Colors`

    4.1 Em `Presets` selecione `Tango`

5. Em `General`, em `Text color:` selecione a cor `Dourada` para que fique visível.


### 1.2 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install zsh -y
    ```


## 2. Habilitar o `autosuggestions` (auto-sugestões ou auto-completar) no `oh-my-zsh`

O recurso que você está descrevendo é conhecido como `autosuggestions` (auto-sugestões ou auto-completar), que exibe comandos anteriores que você digitou que começam com o que você está digitando atualmente. No `oh-my-zsh`, isso geralmente é realizado pelo plugin `zsh-autosuggestions`, você pode instalar o plugin manualmente.

Aqui estão as etapas para instalar o plugin `zsh-autosuggestions` sem usar o Oh My `oh-my-zsh`:

1. **Clone o Repositório do Plugin:** Abra um terminal e execute o seguinte comando para clonar o plugin para o diretório de plugins do `oh-my-zsh`: `git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions`

2. **Adicione o Plugin ao Seu Arquivo `.zshrc`:** Você precisará adicionar uma linha ao seu arquivo `.zshrc` para carregar o plugin. Abra o arquivo `.zshrc` com um editor de texto: `sudo nano ~/.zshrc`

3. **E adicione a seguinte linha no final do arquivo:**

    ```
    plugins=(git sudo zsh-autosuggestions)
    source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
    ``````

4. **Configure as Cores das Sugestões (opcional):** Se você quiser personalizar a cor das sugestões para que sejam mais claras ou correspondam ao seu esquema de cores do terminal, adicione o seguinte ao seu `.zshrc`: `ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=10'`

    Ajuste o valor `'fg=10'` (compatível com o esquema de cores `Tango`) para a cor desejada conforme as configurações do seu terminal.

5. **Recarregue o Seu Arquivo `.zshrc`:** Depois de salvar suas alterações, você pode recarregar o arquivo de configuração com: `source ~/.zshrc`

6. **Verifique se Está Funcionando:** Após recarregar o arquivo `.zshrc`, comece a digitar um comando que você usou anteriormente. As sugestões devem aparecer automaticamente.

Após realizar esses passos, quando você começar a digitar um comando no terminal, o plugin `zsh-autosuggestions` mostrará sugestões com base nos seus comandos anteriores, com a sugestão exibida em uma cor mais clara. Você pode aceitar a sugestão pressionando a tecla de seta para a direita.

Espero que isso ajude a configurar as auto-sugestões no seu terminal `oh-my-zsh`. Se você encontrar algum problema, certifique-se de que o caminho para o script `zsh-autosuggestions`.zsh está correto e que o plugin foi clonado para o local correto.

Se você estiver usando o `bash` e quiser um recurso similar, você precisaria de uma configuração diferente, já que o `zsh-autosuggestions` é específico para o `oh-my-zsh`. No `bash`, o recurso mais próximo é o `history search`, que pode ser habilitado com algumas configurações no arquivo `.bashrc`.


## 3. Alterar o símbolo que aparece entre o nome de usuário e o `host`

Para alterar o símbolo que aparece entre o seu nome de usuário e o nome do `host` no seu prompt do `oh-my-zsh`, você precisará modificar a variável `PROMPT` (ou `PS1` em alguns casos) no seu arquivo `.zshrc`.

1. **Abra o arquivo `.zshrc` no editor de texto:** `sudo nano ~/.zshrc`

2. Localize a parte do arquivo onde a variável `PROMPT` é definida. Você mencionou que quer mudar o símbolo de `㉿` para `@`. Você deve procurar por uma linha que tenha algo similar a isto:

    ```
    configure_prompt() {
    prompt_symbol=@ # ESTA É A LINHA QUE DEVE SER ALTERADA
    # Skull emoji for root terminal
    #[ "$EUID" -eq 0 ] && prompt_symbol=💀
    case "$PROMPT_ALTERNATIVE" in
        twoline)
            PROMPT=$'%F{%(#.blue.green)}┌──${debian_chroot:+($debian_chroot)─}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))─}(%B%F{%(#.red.blue)}%n'$prompt_symbol$'%m%b%F{%(#.blue.green)})-[%B%F{reset}%(6~.%-1~/…/%4~.%5~)%b%F{%(#.blue.green)}]\n└─%B%(#.%F{red}#.%F{blue}$)%b%F{reset} '
            # Right-side prompt with exit codes and background processes
            #RPROMPT=$'%(?.. %? %F{red}%B⨯%b%F{reset})%(1j. %j %F{yellow}%B⚙%b%F{reset}.)'
            ;;
        oneline)
            PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{%(#.red.blue)}%n@%m%b%F{reset}:%B%F{%(#.blue.green)}%~%b%F{reset}%(#.#.$) '
            RPROMPT=
            ;;
        backtrack)
            PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{red}%n@%m%b%F{reset}:%B%F{blue}%~%b%F{reset}%(#.#.$) '
            RPROMPT=
            ;;
    esac
    unset prompt_symbol
    }
    ```

3. **Altere o `㉿` para `@` assim:** `prompt_symbol=@`

4. Salve o arquivo e saia do editor (em `nano`, você faz isso com `Ctrl+X`, confirma as mudanças com `Y` e depois pressiona `Enter`).

5. Depois de salvar o arquivo, você pode aplicar as alterações imediatamente com: `source ~/.zshrc`

    Ou simplesmente fechar e reabrir o terminal.


## 5. Mudar o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando

1. Finalmente, mude o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando: `sudo chsh -s /bin/bash`

    Você precisará fechar a sessão e logar novamente para que a alteração tenha efeito.

2. **Iniciar o `bash` Manualmente:** Caso NÃO funcione, como solução temporária, você pode iniciar o `bash` manualmente em um terminal do `oh-my-zsh`, simplesmente digitando bash. Isso não muda seu `shell` padrão, mas inicia uma sessão do `bash` naquele terminal específico.


## 6. Alterar a opacidade/transparência do `Terminal Emulator`

A referência específica à transparência padrão do terminal no `Kali Linux` não é mencionada diretamente nas fontes. No entanto, uma prática comum é definir a transparência do painel do terminal para cerca de `5%`, para dar uma aparência estilizada, como mencionado em um guia de personalização do ambiente de desktop `xfce` no `Kali Linux​​`. Isso indica que a transparência padrão pode ser definida para um valor baixo ou até mesmo desativada por padrão, com a opção de ajuste conforme a preferência do usuário.

No entanto, se você deseja ajustar ou verificar a transparência do seu terminal no Kali Linux, você geralmente pode fazer isso através das preferências do próprio terminal. Por exemplo, no GNOME Terminal, você pode seguir estes passos:

1. Abra o `Terminal Emulator`.

2. Clique com o botão direito dentro do terminal e selecione `“Preferences”` ou `“Profile Preferences”`.

3. Na aba `“Appearance”`, você encontrará um controle deslizante para ajustar a opacidade/transparência do fundo do terminal.

É importante observar que essas configurações podem variar dependendo do emulador de terminal que você está usando. Além disso, a capacidade de ajustar a transparência pode depender de outros fatores do sistema, como os efeitos gráficos habilitados no seu ambiente de desktop.

7. Desinstalar o `shell` `oh-my-zsh`

Para desinstalar o zsh e limpar as configurações no Ubuntu pelo terminal, você pode seguir estes passos:

1. **Desinstalar o `oh-my-zsh`:** `sudo apt remove --purge zsh`

2. **Remover as configurações pessoais:** Apague o diretório de configuração do `oh-my-zsh` no seu diretório `home`: `rm -rf ~/.zsh ~/.zshrc`

3. **Mudar o `shell` padrão de volta para o `bash`**: Para voltar para o `bash` como seu `shell` padrão, execute: `chsh -s /bin/bash`

Lembre-se de que você precisará fechar e reabrir o terminal ou reiniciar a sessão para que as alterações entrem em vigor. Isso removerá o zsh e suas configurações do seu sistema.


## 7. Desinstalar o `oh-my-zsh`

Para desinstalar completamente o `oh-my-zsh` no `Linux Ubuntu`, você precisa seguir algumas etapas. Primeiro, é importante remover o pacote `oh-my-zsh` em si e, em seguida, alterar o `shell` padrão para o usuário de volta ao `shell` anterior (geralmente `bash`), caso o `oh-my-zsh` tenha sido configurado como o `shell` padrão. Aqui estão as etapas detalhadas:

1. **Abra o terminal:** Você pode fazer isso pressionando no `Ubuntu`: `Ctrl + Alt + T`

2. Verifique se o `oh-my-zsh` é o `shell` atual: Antes de desinstalar o `oh-my-zsh`, é uma boa ideia verificar se ele está configurado como o `shell` padrão para o seu usuário. Execute: `echo $SHELL`

3. Se o resultado for algo como `/usr/bin/zsh` ou similar, significa que `oh-my-zsh` é o seu `shell` atual.

4. Troque o `shell` padrão para bash (ou outro `shell` de sua preferência): Se `oh-my-zsh` é o seu `shell` atual, você precisa mudá-lo antes de desinstalar o `oh-my-zsh`. Para mudar para `bash`, por exemplo, use: `chsh -s /bin/bash
`
5. Você precisará sair e entrar novamente na sua sessão para que a alteração tenha efeito.

6. **Desinstale o `oh-my-zsh`:** Agora, para desinstalar o `oh-my-zsh`, use o comando `apt` com privilégios de administrador: `sudo apt remove --purge zsh`

7. Este comando remove o `oh-my-zsh` e qualquer configuração personalizada que você possa ter feito.

8. **Limpe os pacotes não mais necessários:** Após a desinstalação, é uma boa prática remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários: `sudo apt autoremove`

9. **Opcional - Remova manualmente qualquer arquivo de configuração residuais:** Se você quiser garantir que todas as configurações personalizadas do `zsh` sejam removidas, pode precisar excluí-las manualmente. Arquivos de configuração do `zsh` geralmente estão localizados em seu diretório home, como .zshrc. Para removê-los, use: `rm ~/.zshrc`

    E qualquer outro arquivo de configuração do `zsh` que você possa ter criado ou modificado.

Lembre-se de que esses comandos podem variar ligeiramente dependendo da sua configuração específica e da versão do `Ubuntu`. Certifique-se de ter backups de quaisquer dados ou configurações importantes antes de proceder com a desinstalação.

## Referências

[1] OPENAI. ***Configurando terminal no ubuntu.*** Disponível em: <https://chat.openai.com/c/1ecf460a-8fee-4048-9a29-baae6a494efd> (texto adaptado). ChatGPT. Acessado em: 07/12/2023 09:07.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 29/11/2023 09:07.

[3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830>. ChatGPT. Acessado em: 15/12/2023 08:25.

[4] USER: LEO VARGAS. Como personalizar o terminal do linux - mais produtivo e bonito. Disponĩvel em: <https://www.youtube.com/watch?v=zqrUlHA8jTA&t=1s>. Acessado em: 05/06/2024 16:26.
