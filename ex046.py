'''Faça um programa que mostre ma tela uma contagem regressiva para o estouro de fogos de artificio, indo do 10 ao 0,
com uma pausa de 1 segundo entre eles'''
from time import sleep
print('A CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFICIOS COMEÇA AGORA EM: ')
sleep(1)
for cont in range (10, -1, -1):
    print('{0}' .format(cont))
    sleep(1)

print('FELIZ ANO NOVO!!!!! 🌟🎇🥳')
sleep(1)
print('''           *     .        *  .  *    .   *
     .     .   *    .     .    *     .    *
  *   .    *       *    .      *   .   .     *
     .    *   * .    .   *   .    *  .    *
     *    .     .   .     *    *   .     .   *
   *   .     * .     .   *  .    .     *   . *
   .     .   *   *    .    *   .   .    .   .
*    .    *     .   *    *  .     .      *    *
        .     .    *  .     .   *   *    .     .
    .      *    .    *    .   *    .   *     .
      *   .    .    * .   *      .    .     *
      .    *   *    .    .  *   .   *   .    .
        .    *   .     .   *    .     *   .
  *     .     .  .  *  .   .   *      *    .
            * .     .  *    .   *  .   *   .
     .    *   .      .    *    .     .    *
            *    .  *     .   .   *    .     .
  *    .  *    .     .     .    *   .     .   ''')
