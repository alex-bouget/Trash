exec("import string\nimport random\nimport pytmx", globals())
def procedural_Map(self):
    class Procedural:
        def seed_generator(self, height):
            return "".join([random.choice(string.ascii_letters) for x in range(height)])
        def generating_chunk_data(self, chunk_x, chunk_y, seed): #for me: 1025; 1025
            #/\ x
            #|
            # -->  y
            """chunk_x: Number of chunk in x coordonates
            chunk_y: Number of chunk in y coordonates
            seed: Seed for map"""
            def noise(chunk_x, chunk_y, seed):
                noise_map = []
                top_of_range = 0
                bottom_of_range = 0
                for x in range(chunk_x):
                    new_row = []
                    for y in range(chunk_y):
                        new_value=0
                        print(str(x)+", "+str(y))
                        if x==0 and y==0:
                            new_value = random.randint(-1000, +1000)
                        elif x == 0:
                            new_value = new_row[-1] + random.randint(-1000, +1000)
                        elif y == 0:
                            new_value = noise_map[x-1][y] + random.randint(-1000, +1000)
                        else:
                            temp = random.randint(0, 2)
                            if temp == 0:
                                new_value = new_row[-1] +random.randint(-1000, +1000)
                            elif temp == 1:
                                new_value = noise_map[x-1][y] +random.randint(-1000, +1000)
                            else:
                                minimum = min(new_row[-1], noise_map[x-1][y])
                                maximum = max(new_row[-1], noise_map[x-1][y])
                                average_value = minimum + ((maximum-minimum)/2.0)
                                new_value = average_value + random.randint(-1000, +1000)
                        new_row.append(new_value)
                        if new_value > top_of_range:
                            top_of_range = new_value
                        if new_value < bottom_of_range:
                            bottom_of_range = new_value
                    noise_map.append(new_row)
                difference = float(top_of_range - bottom_of_range)
                for x in range(len(noise_map)):
                    for y in range(len(noise_map[0])):
                        noise_map[x][y] = (noise_map[x][y] - bottom_of_range) / difference
                return noise_map
            random.seed(seed)
            humidity = noise(chunk_x, chunk_y, seed)
            latitude = noise(chunk_x, chunk_y, seed)
            temperature = noise(chunk_x, chunk_y, seed)

            chunk_data = []
            for x in range(chunk_x):
                new_row = []
                for y in range(chunk_y):
                    new_row.append({"humidity": humidity[x][y], "temperature": temperature[x][y], "latitude": latitude[x][y]})
                chunk_data.append(new_row)
            return chunk_data
    return Procedural()



