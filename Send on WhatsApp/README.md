## Automação para envio de mensagens por WhatsApp ##
- Sistema criado na intenção de ser um método alternativo da opção do **WhatsApp Buniness**;
- Funciona com planilha do Excel contendo a princípio em ordem: número de celular e nome
- Necessita que o ``'chromedriver'`` esteja presente na mesma pasta origem

## Execução ##
Ao executar o código, será inicializado uma tela do ``PyAutoGUI`` na qual escolherá um arquivo Excel __(.xlsx)__ e clicará em seguida no botão ``Enviar``
Será aberto uma tela no navegador para que seja escaneado o QR Code do ``WhatsApp Web``, após isso, será feito os envios e quando terminar, aparecerá uma mensagem ``Enviado com sucesso!`` no canto inferitor abaixo do botão ``Enviar``
