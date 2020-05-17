from pygame import font


class Node:
    def __init__(self, index, connections, description, display):
        self.node_font = font.Font('freesansbold.ttf', 16)
        self.display = display
        self.id = index
        self.connections = connections
        self.description = description

    def draw(self, selected_index):
        lines_counter = 1
        string = ""
        for char_index in range(int(len(self.description))):
            string += self.description[char_index]
            if len(string) > 50 and self.description[char_index] == " ":
                text = self.node_font.render(string, False, (255, 0, 0))
                self.display.blit(text, (50, 25 * lines_counter))
                lines_counter += 1
                string = ""
        text = self.node_font.render(string, False, (255, 255, 255))
        self.display.blit(text, (50, 25 * lines_counter))

        # zakomentowac
        for key in self.connections:
            if not self.connections[key]["is_active"]:
                continue
            if selected_index == int(key):
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            text = self.node_font.render(self.connections[key]["decision"], False, color)
            self.display.blit(text, (50, (lines_counter + 2) * 25))
            lines_counter += 1
