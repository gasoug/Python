## Automação para envio de email com anexo em pdf ##
- A proposta do código é para a necessidade de envio de arquivos diferentes para diferentes contatos, baseado em um tipo de lista em csv. Como exemplo, pode ser usado para um envio de boletos;
- Há a possibilidade de usar o mesmo código para o Excel, por exemplo, alterando o tipo de arquivo e biblioteca importada;
- Dentro do código está explicando todos os campos que será preciso alteração;
- Referente a senha, é a senha que é gerado no google, acessando a conta, clicando na aba "Segurança" e descendo até a parte de "Senhas de APP" e realizar o processo que gera essa senha;
- Há um campo de "controle" para não enviar a mesma fatura 2 vezes, que seria o "Status", estando diferente de "Enviado", nesse exemplo, o boleto será enviado. Para a não duplicicade, basta apenas preencher na coluna como "Enviado";
- É necessário que tanto na tabela quanto no arquivo do anexo, o nome seja exatamente o mesmo, caso contrário, não irá encontrar o arquivo para anexar;