from pygame import font


class Node:
    def __init__(self, index, connections, description, display):
        self.node_font = font.Font('freesansbold.ttf', 16)
        self.display = display
        self.id = index
        self.connections = connections
        self.description = description

    def __str__(self):
        connections = ""
        for key in self.connections:
            connections += "{} {}\n".format(self.connections[key]["target_node_id"], self.connections[key]["decision"])

        return "Index: {}\nDescription: {}\n".format(self.id, self.description) + connections

    def draw(self, selected_index):
        line_length = 50
        lines_counter = 1
        iterations = int(len(self.description) / line_length)
        for x in range(iterations):
            text = self.node_font.render(self.description[x * line_length: (x + 1) * line_length], False,
                                         (255, 255, 255))
            self.display.blit(text, (50, 25 * lines_counter))
            lines_counter += 1
        text = self.node_font.render(self.description[iterations * line_length:], False, (255, 255, 255))
        self.display.blit(text, (50, 25 * lines_counter))

        for key in self.connections:
            if selected_index == int(key):
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            text = self.node_font.render(key + ". " + self.connections[key]["decision"], False, color)
            self.display.blit(text, (50, (lines_counter + 2) * 25))
            lines_counter += 1
