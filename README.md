# Como configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos para configurar/instalar/usar o `oh-my-zsh` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands for configuring/installing/use `oh-my-zsh` on `Linux Ubuntu`._

## Descrição [2]

### `shell`

Um `shell` é uma Interface de Linha de Comando (_Command Line Interface, CLI_) que permite aos usuários interagirem com um sistema operacional por meio de comandos de texto. Ele interpreta os comandos inseridos pelo usuário e os executa, facilitando a manipulação de arquivos, a execução de programas e outras tarefas do sistema. Além disso, os shells também oferecem recursos avançados, como redirecionamento de entrada e saída, expansão de comandos e controle de processos. Exemplos comuns incluem o `Bash`, o `Zsh` e o `PowerShell`.


### `bash`

`Bash`, ou `Bourne Again Shell`, é um `shell` de linha de comando amplamente utilizado em sistemas operacionais Unix e `Linux`. Ele oferece uma variedade de recursos, como expansão de comandos, redirecionamento de entrada/saída, _scripts_ de `shell` e controle de processos. O `Bash` é altamente personalizável e suporta automação de tarefas por meio de _scripts_, tornando-o uma ferramenta poderosa para usuários avançados e administradores de sistemas. Sua sintaxe simples e intuitiva o torna acessível para iniciantes, enquanto sua flexibilidade e extensibilidade o tornam uma escolha popular entre profissionais de TI.


### `zsh`

O `oh-my-zsh`, ou `Z Shell`, é um interpretador de `shell` de código aberto e uma alternativa avançada ao `bash` (`Bourne Again Shell`), que é comumente usado em sistemas Unix e Linux. O `oh-my-zsh` oferece uma série de recursos avançados, como autocompletamento poderoso, histórico de comandos expandido, personalização flexível da aparência e do comportamento do `shell`, além de suporte a plugins e temas. Sua interface de linha de comando aprimorada e recursos de automação tornam-no uma escolha popular entre desenvolvedores, administradores de sistema e entusiastas de terminal que desejam uma experiência de linha de comando mais produtiva e personalizável. O `oh-my-zsh` é altamente configurável e pode ser estendido por meio de plugins, tornando-o uma ferramenta versátil para trabalhar com eficiência no ambiente `Unix` e `Linux`.


### `oh-my-zsh`

`Oh-my-zsh` é um _framework_ de código aberto para gerenciar a configuração do _shell_ `Zsh`, fornecendo um conjunto de plugins, temas e ferramentas para aprimorar a experiência do usuário. Ele simplifica a personalização do ambiente de linha de comando, oferecendo recursos como autocompletar, atalhos de teclado e sugestões contextuais, aumentando a produtividade e a eficiência dos usuários. Com uma comunidade ativa e uma grande variedade de extensões disponíveis, o `Oh-my-zsh` é amplamente utilizado por desenvolvedores e usuários avançados para customizar e otimizar o ambiente de terminal.


### `powerlevel10k`

O `Powerlevel10k` é um tema altamente configurável para o terminal `Zsh`, conhecido por sua velocidade e eficiência. Ele oferece uma experiência personalizável ao usuário, com uma configuração inicial rápida e opções avançadas para ajustar o estilo e os elementos exibidos no prompt de comando. O `Powerlevel10`k suporta ícones, diferentes estilos de prompt, exibição de informações contextuais e é projetado para ser rápido mesmo em ambientes com muitos plugins e configurações adicionais.


### `zinit`

O `Zinit` é um gerenciador de plugins e temas para o `Zsh`, projetado para simplificar e otimizar o processo de personalização do ambiente de linha de comando. Com recursos avançados de carregamento assíncrono, ele oferece uma inicialização rápida do shell, permitindo aos usuários instalar e atualizar facilmente extensões, temas e utilitários adicionais. Além disso, o `Zinit` suporta a configuração flexível de plugins, garantindo compatibilidade com diferentes workflows e necessidades de desenvolvimento. Com uma sintaxe intuitiva e uma vasta biblioteca de extensões disponíveis, o `Zinit` é uma ferramenta poderosa para aumentar a produtividade e a eficiência dos usuários do Zsh.


### `zsh-completions`

O `zsh-completions` é um _plugin_ para o `shell` `zsh` que sugere automaticamente comandos com base no histórico de entrada do usuário. Ele funciona destacando uma sugestão na linha de comando, baseada no que o usuário começou a digitar, facilitando a reutilização de comandos anteriores de maneira eficiente. Isso não apenas economiza tempo, mas também reduz erros ao lembrar comandos frequentemente usados.


### `zsh-completions`

O `zsh-completions` é um conjunto de _scripts_ de conclusão automática para o `shell` `zsh`, projetado para melhorar a experiência do usuário ao fornecer conclusões detalhadas e precisas para comandos, argumentos de comandos e opções. Ele amplia significativamente a funcionalidade do `shell` `zsh`, permitindo que os usuários completem rapidamente comandos complexos e evitem erros de sintaxe, aumentando assim a eficiência na linha de comando.


### `fast-syntax-highlighting`

O `fast-syntax-highlighting` é um _plugin_ para o `shell` `fish` que oferece realce de sintaxe rápido e responsivo para comandos e scripts. Ele melhora a experiência do usuário ao proporcionar cores distintas para diferentes elementos de linguagem, facilitando a leitura e a compreensão de código diretamente no terminal. Essa funcionalidade ajuda os usuários a identificar erros de sintaxe mais rapidamente e a escrever scripts de forma mais eficiente no `shell` `fish`.


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
    

### 1.1 Configurar/Instalar/Usar o `oh-my-zsh`

Para configurar/instalar/usar o `oh-my-zsh` em um sistema `Linux Ubuntu`, você pode seguir estes passos:

1. Primeiro, instale o `oh-my-zsh` com o comando: `sudo apt install zsh -y`

2. **Instalar os pacotes `curl` e `git`**: `sudo apt install curl git -y`

3. **Instalar o `oh-my-zsh`**: `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório: `sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/ /home/edenedfsls/`
    

### 1.2 Configurar o `zsh` como seu `shell` padrão

1. **Configurar o `zsh` como seu `shell` Padrão:** Para configurar o `zsh` como seu `shell` padrão, use (**NÃO** colocar o `sudo`!): `chsh -s $(which zsh)`

    - Você precisará fazer _logout_ e _login_ novamente para que a mudança tenha efeito.

2. **Criar o Arquivo .`zshrc`:** Se, por algum motivo, o arquivo `.zshrc` **NÃO** for criado automaticamente, você pode criá-lo manualmente: `sudo nano ~/.zshrc`

    - Adicione as configurações que deseja e salve o arquivo.

3. **Aplicar as alterações:** Para que as mudanças tenham efeito, você precisa recarregar o arquivo de configuração. Isso pode ser feito com o comando: `source ~/.zshrc`

    Ou simplesmente feche e reabra o terminal.

Esses passos devem ajudar a configurar o `zsh` com o tema e os plugins desejados. Se tiver dificuldades com algum plugin específico, pode ser útil consultar a documentação do `Oh My Zsh` ou procurar ajuda específica para aquele _plugin_.


### 1.3 Código completo para configurar/instalar/usar

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
    sudo apt install curl git -y
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```


### 2. Configurar/Instalar/Usar o `zinit`

1. **Instalar o `zinit`**: `bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"`

    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/.local/share/`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório: `sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/ /home/edenedfsls/.local/share/`
    
2. **Abrir o arquivo `~/.zshrc`**: `sudo nano ~/.zshrc`

3. **Editar o arquivo `~/.zshrc`**:

    ```
    # Adicionar no final do .zshrc
    zinit light zdharma-continuum/fast-syntax-highlighting
    zinit light zsh-users/zsh-autosuggestions
    zinit light zsh-users/zsh-completions
    ```

    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/.local/share/`

    Segue a lista de arquivos que a pasta deve possuir:

    - `_local---zinit`
    
    - `zdharma-continuum---fast-syntax-highlighting`
    
    - `zdharma-continuum---zinit-annex-as-monitor`
    
    - `zdharma-continuum---zinit-annex-bin-gem-node`
    
    - `zdharma-continuum---zinit-annex-patch-dl`
    
    - `zdharma-continuum---zinit-annex-rust`
    
    - `zdharma---fast-syntax-highlighting`
    
    - `zsh-users---zsh-autosuggestions`
    
    - `zsh-users---zsh-completions`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório:
    
    ```
    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/zinit/ /home/edenedfsls/.local/share/zinit/

    sudo cp -R "/home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/zdharma-continuum---fast-syntax-highlighting/" /home/edenedfsls/.local/share/zinit/plugins/

    sudo cp -R "/home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/zdharma---fast-syntax-highlighting/" /home/edenedfsls/.local/share/zinit/plugins/
    ```

4. Fechar o `Terminal Emulator` e abrir novamente


### 3. Configurar/Instalar/Usar a fonte `fira code`

1. **Criar diretório**: `mkdir ~/.fonts`

2. **Baixar fonte**: `wget -P ~/.fonts 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/BitstreamVeraSansMono.zip'` 

3. **Descompactar fonte**: `unzip ~/.fonts/BitstreamVeraSansMono.zip -d ~/.fonts`

    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório: `sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/.fonts/ /home/edenedfsls/.fonts/` 

4. **Instalar a fonte `firacode`**: `sudo apt install fonts-firacode -y`

5. Fechar o `Terminal Emulator` e abrir novamente

6. Clicar na aba: `Edit`

7. Clicar em `Preferences...`

8. No campo `Font` clicar na fonte e alterar para `Fira Code Regular`


### 4. Configurar/Instalar/Usar o tema `powerlevel10k`

1. **Instalar o tema `powerlevel10k`**: `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k`

    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/.oh-my-zsh/themes/`

    1.1 Copiar a pasta também para o diretório: `/home/edenedfsls/`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório:
    
    ```
    sudo cp -R /home/edenedfsls/.oh-my-zsh/themes/ /home/edenedfsls/
    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/powerlevel10k/ /home/edenedfsls/
    ```

2. **Inserir o `powerlever10k` no arquivo de configuração do `zshrc`**: `echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc`

3. **Abrir o arquivo `~/.zshrc`**: `sudo nano ~/.zshrc`

4. **Editar o arquivo `~/.zshrc` alterar a linha, como segue**: `ZSH_THEME="powerlevel10k/powerlevel10k"`

5. Fechar o `Terminal Emulator` e abrir novamente


#### 4.1 Copiar demais arquivos antes de configurar o `powerlevel10k`

1. **Copiar o(s) arquivo(s) de configuração**:

    Segue a lista de arquivos a serem copiados:

    - `.p10k.zsh`
    
    - `.zsh_history`
    
    - `.zshrc.pre-oh-my-zsh`
    
    - `.zshrc`
       
    **OBSERVAÇÂO(ÕES)**: O diretório para a pasta ou arquivo é indicado a seguir, conferir se no diretório se a(s) pasta(s) e/ou o(s) arquivo(s) existe(m), se não, copiar da pasta `docs` para o diretório: `/home/edenedfsls/`

    Você pode usar o código a seguir para copiar a pasta ou o arquivo para o diretório:
    
    ```
    # REALIZAR BACKUP DOS ARQUIVOS EXISTENTES:

    # Define a variável com a data e hora atual
    timestamp=$(date +"_backup_%m_%d_%Y_%H_%M_%S")

    # Copiar os arquivos de configuração adicionando o timestamp ao nome do arquivo
    cp /home/edenedfsls/.p10k.zsh /home/edenedfsls/.p10k.zsh$timestamp
    cp /home/edenedfsls/.zsh_history /home/edenedfsls/.zsh_history$timestamp
    cp /home/edenedfsls/.zshrc.pre-oh-my-zsh /home/edenedfsls/.zshrc.pre-oh-my-zsh$timestamp
    cp /home/edenedfsls/.zshrc /home/edenedfsls/.zshrc_linux_ubuntu$timestamp

    # COPIAR OS NOVOS ARQUIVOS:
    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/.p10k.zsh /home/edenedfsls/

    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/.zsh_history /home/edenedfsls/

    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/.zshrc.pre-oh-my-zsh /home/edenedfsls/

    sudo cp -R /home/edenedfsls/Documents/Downloads/unix/ubuntu/oh_my_zsh/docs/.zshrc /home/edenedfsls/
    ```

#### 4.2 Configurar o `powerlevel10k`

1. Confirmar os símbos que estiver vendo para que a configuração reconheca e configure corretamente.

2. Em `Prompt Style` escolha a opção:  `(3) Rainbow.`

3. Em `Character Set` escolha a opção:  `(1) Unicode.`

4. Em `Show current time?` escolha a opção:  `(2) 24-hour format.`

5. Em `Prompt Separators` escolha a opção:  `(1) Angled.`

6. Em `Prompt Heads` escolha a opção:  `(3) Sharp.`

7. Em `Prompt Tails` escolha a opção:  `(2) Bluerred.`

8. Em `Prompt Height` escolha a opção:  `(2) Two lines.`

9. Em `Prompt Connection` escolha a opção:  `(3) Solid.`

10. Em `Prompt Frame` escolha a opção:  `(2) Left.`

11. Em `Connection & Frame Color` escolha a opção:  `(1) Lightest.`

12. Em `Prompt Spacing` escolha a opção:  `(2) Sparse.`

13. Em `Icons` escolha a opção:  `(2) Many icons.`

14. Em `Prompt Flow` escolha a opção:  `(2) Fluent.`

15. Em `Enable Transient Prompt` escolha a opção:  `(n) No.`

16. Em `Instant Prompt Mode` escolha a opção:  `(1) Verbose (recommended).`

17. Em `Apply changes to ~/.zshrc` escolha a opção:  `(y) Yes (recommended).`


### 4.3 Ajustes

#### 4.3.1 Ajustar as cores do `Terminal Emulator`

1. No `Terminal Emulator`, na barra de ferramentas, clicar em: `Edit`

2. Clique em: `Preferences`

3. Clique na aba `Appearence`

    3.1 Em `Background` altere a opção para `Transparent background`

    3.2 Em `Opacity` coloque em `0.85`

4. Clique na aba `Colors`

    4.1 Em `Presets` selecione `Tango`

5. Em `General`, em `Text color:` selecione a cor `Dourada` para que fique visível.


### 4.4 Reconfigurar o `powerlevel10k`

1. Para reconfigurar o `Powerlevel10k` no `Zsh`, você pode executar o comando de configuração fornecido pelo próprio tema. Abra o terminal e digite o seguinte: `p10k configure`

Isso iniciará o assistente de configuração do `Powerlevel10k`, onde você poderá escolher várias opções para personalizar o visual e o comportamento do seu `prompt` de comando. Se você tiver algum arquivo de configuração anterior, como `~/.p10k.zsh`, o assistente pode usar essas configurações como base ou você pode começar uma nova configuração do zero.

## 5. Mudar o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando

1. Finalmente, mude o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando: `sudo chsh -s /bin/bash`

    Você precisará fechar a sessão e logar novamente para que a alteração tenha efeito.

2. **Iniciar o `bash` Manualmente:** Caso **NÃO** funcione, como solução temporária, você pode iniciar o `bash` manualmente em um terminal do `oh-my-zsh`, simplesmente digitando bash. Isso não muda seu `shell` padrão, mas inicia uma sessão do `bash` naquele terminal específico.


## 6. Alterar a opacidade/transparência do `Terminal Emulator`

A referência específica à transparência padrão do terminal no `Kali Linux` não é mencionada diretamente nas fontes. No entanto, uma prática comum é definir a transparência do painel do terminal para cerca de `5%`, para dar uma aparência estilizada, como mencionado em um guia de personalização do ambiente de desktop `xfce` no `Kali Linux​​`. Isso indica que a transparência padrão pode ser definida para um valor baixo ou até mesmo desativada por padrão, com a opção de ajuste conforme a preferência do usuário.

No entanto, se você deseja ajustar ou verificar a transparência do seu terminal no `Kali Linux`, você geralmente pode fazer isso através das preferências do próprio terminal. Por exemplo, no GNOME Terminal, você pode seguir estes passos:

1. Abra o `Terminal Emulator`.

2. Clique com o botão direito dentro do terminal e selecione `“Preferences”` ou `“Profile Preferences”`.

3. Na aba `“Appearance”`, você encontrará um controle deslizante para ajustar a opacidade/transparência do fundo do terminal.

É importante observar que essas configurações podem variar dependendo do emulador de terminal que você está usando. Além disso, a capacidade de ajustar a transparência pode depender de outros fatores do sistema, como os efeitos gráficos habilitados no seu ambiente de desktop.

## 7. Adicionar o ícone da cobra (`Python`) no _prompt_ do tema `Powerlevel10k` em `zsh` 

Para adicionar o ícone da cobra (`Python`) no _prompt_ do tema `Powerlevel10k` em `zsh`, você precisa configurar o segmento do ambiente {{Python}} (como o `pyenv`, `virtualenv`, `anaconda` etc.) para incluir um ícone. Aqui estão os passos gerais:

1. **Acesse o Arquivo de Configuração**: Abra o arquivo `~/.p10k.zsh` em um editor de texto. Esse arquivo é gerado pelo `Powerlevel10k` quando você configura o tema pela primeira vez com `p10k configure`.

2. **Localize o Segmento de Configuração Python**: Procure a seção que configura o ambiente `Python` que você está usando. Por exemplo, se você estiver usando `virtualenv`, procure por configurações que começam com `POWERLEVEL9K_VIRTUALENV_`.

3. **Adicionar ou modificar o ícone**: Adicione ou altere a linha que define o ícone. Por exemplo, para `virtualenv`, você pode adicionar: `typeset -g POWERLEVEL9K_VIRTUALENV_VISUAL_IDENTIFIER_EXPANSION='🐍'`

    Isso definirá o ícone da cobra para o ambiente virtual `Python`.

4. **Aplicar as mudanças**: Depois de fazer as alterações, salve o arquivo e reinicie o `Terminal Emulator` ou recarregue sua configuração com: `source ~/.zshrc`

5. Reinicie o computador.

Se o ícone da cobra não aparecer após essas configurações, certifique-se de que seu `Terminal Emulator` suporta emojis e que as configurações do `Powerlevel10k` estão corretas para exibir ícones.


## 8. Desinstalar o `oh-my-zsh`

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

9. **Opcional - Remova manualmente qualquer arquivo de configuração residuais:** Se você quiser garantir que todas as configurações personalizadas do `zsh` sejam removidas, pode precisar excluí-las manualmente. Arquivos de configuração do `zsh` geralmente estão localizados em seu diretório home, como `.zshrc`. Para removê-los, use: `rm ~/.zshrc`

    E qualquer outro arquivo de configuração do `zsh` que você possa ter criado ou modificado.

Lembre-se de que esses comandos podem variar ligeiramente dependendo da sua configuração específica e da versão do `Linux Ubuntu`. Certifique-se de ter _backups_ de quaisquer dados ou configurações importantes antes de proceder com a desinstalação.

## Referências

[1] OPENAI. ***Configurando terminal no ubuntu.*** Disponível em: <https://chat.openai.com/c/1ecf460a-8fee-4048-9a29-baae6a494efd> (texto adaptado). ChatGPT. Acessado em: 07/12/2023 09:07.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 29/11/2023 09:07.

[3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830>. ChatGPT. Acessado em: 15/12/2023 08:25.

[4] USER: LEO VARGAS. ***Como personalizar o terminal do linux - mais produtivo e bonito.*** Disponĩvel em: <https://www.youtube.com/watch?v=zqrUlHA8jTA&t=1s>. Acessado em: 05/06/2024 16:26.
