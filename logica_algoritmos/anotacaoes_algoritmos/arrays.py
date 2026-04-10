'''
Array é um espaço continuo na memória

Um ponteiro com a localização exata do inicio de um array na memoria é armazenado.
Caso queira acessar um valor qualquer desse array, o computador n precisa varrer o espaço inteiro na memoria, basta ele ir direto na posição
    -> Por isso que acessar um valor de um array é O(1), pois é instantaneo, independente do tamanho do array

Caso queira aumentar o número de dados em um array, é necessario que o computador instancie o array em outra posição na memória.
    -> Isso ocorre porque array é continuo, o espaço ao lado desse array pode estar sendo ocupado, então todo o array vai para uma nova posição.
    -> Nesse caso, pode ocorrer em O(n) caso todo o array tenha que alterar o "endereço"
        -> O mesmo ocorre ao adicionar valores no inicio ou meio do Array, pois o index de todos os itens do array vão mudar de posição.
'''
