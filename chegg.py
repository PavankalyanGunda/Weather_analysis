class Cache:
    def __init__(self, block_size, max_blocks):
        self.blocks = [None] * max_blocks
        self.block_size = block_size
        self.hits = 0
        self.misses = 0

    def get_block(self, memory_address):
        block_number = memory_address // self.block_size
        block = self.blocks[block_number]
        if block is not None:
            self.hits += 1
            return block
        else:
            self.misses += 1
            return None

    def set_block(self, memory_address, block):
        block_number = memory_address // self.block_size
        self.blocks[block_number] = block

    def clear(self):
        self.blocks = [None] * len(self.blocks)

    def get_hit_rate(self):
        return self.hits / (self.hits + self.misses)

    def __str__(self):
        return str([block_number for block_number, block in enumerate(self.blocks) if block is not None])

# Modified version that prints the block numbers of the cache
class CacheModified(Cache):
    def __str__(self):
        return str([block_number for block_number, block in enumerate(self.blocks) if block is not None])


class CPU:
    def __init__(self, cache):
        self.cache = cache
        self.instructions = []

    def read_instruction(self):
        instruction = self.instructions.pop(0)
        block = self.cache.get_block(instruction)
        if block is None:
            block = self.read_block_from_main_memory(instruction)
            self.cache.set_block(instruction, block)
        return block[instruction % self.cache.block_size]

    def execute_instruction(self, instruction):
        # Execute the instruction here
        pass

    def read_block_from_main_memory(self, memory_address):
        # Read the block from main memory here
        pass

    def run(self):
        while self.instructions:
            instruction = self.read_instruction()
            self.execute_instruction(instruction)


def main():
    block_size = 8
    max_blocks = 16

    # Create a cache
    cache = Cache(block_size, max_blocks)

    # Create a CPU
    cpu = CPU(cache)

    # Read the input file
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                if line.startswith("DF1ED334"):
                    cpu.instructions.append(int(line, 16))
                elif line.startswith("CLEAR"):
                    cache.clear()
                elif line.startswith("DEL"):
                    block_number = int(line[3:], 16)
                    cache.blocks[block_number] = None

    # Run the CPU
    cpu.run()

    # Print the output
    print(f"Hit rate: {cache.get_hit_rate()}")
    print(f"Cache: {cache}")

if __name__ == "__main__":
    main()
