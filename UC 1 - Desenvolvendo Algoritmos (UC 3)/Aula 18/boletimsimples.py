notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5]

media = sum(notas) / len(notas)

print(f"""
         BOLETIM
      Maior nota: {max(notas)}
      Menor nota: {min(notas)}
      Média da turma: {media:.1f}
      """)