def find_busiest_period(data):
  pass # your code goes here
  maxTime = time = 0
  people = 0
  max = 0
  if len(data) == 0:
      return 0
  if len(data) == 1:
      return data[0][0]
  for i in range(0, len(data)):

      if data[i][2] == 1:
          people = people + data[i][1]
      else:
          people = people - data[i][1]
      if i < len(data)-1 and data[i][0] == data[i+1][0]:
          continue
      if people > max:
          maxTime = data[i][0]
          max = people

  return maxTime


data = [[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,19,1],[1487801478,1,0],[1487801478,1,1],[1487901013,1,0],[1487901211,7,1],[1487901211,8,0]]
print(find_busiest_period(data))