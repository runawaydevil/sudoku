from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def is_valid(board, row, col, num):
    # Verifica se o número é válido na linha
    if num in board[row]:
        return False
    
    # Verifica se o número é válido na coluna
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Verifica se o número é válido no quadrado 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def count_solutions(board):
    count = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        count += count_solutions([row[:] for row in board])
                        board[row][col] = 0
                return count
    return 1

def generate_sudoku(difficulty=0.5):
    # Cria um tabuleiro vazio
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Preenche a diagonal principal com números aleatórios
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = nums[j*3+k]
    
    # Resolve o tabuleiro completo
    solve_sudoku(board)
    
    # Remove números aleatoriamente baseado na dificuldade
    cells_to_remove = int(81 * difficulty)
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    
    # Garante que o tabuleiro tenha solução única
    for i, j in positions[:cells_to_remove]:
        temp = board[i][j]
        board[i][j] = 0
        
        # Verifica se ainda tem solução única
        if count_solutions([row[:] for row in board]) > 1:
            board[i][j] = temp
    
    return board

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['GET'])
def new_game():
    difficulty = float(request.args.get('difficulty', 0.5))
    board = generate_sudoku(difficulty)
    return jsonify({'board': board})

@app.route('/check_solution', methods=['POST'])
def check_solution():
    data = request.get_json()
    board = data['board']
    
    # Verifica se o tabuleiro está completo
    if any(0 in row for row in board):
        return jsonify({'valid': False, 'message': 'O tabuleiro não está completo!'})
    
    # Verifica se a solução é válida
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            board[i][j] = 0
            if not is_valid(board, i, j, num):
                return jsonify({'valid': False, 'message': 'Solução inválida!'})
            board[i][j] = num
    
    return jsonify({'valid': True, 'message': 'Parabéns! Solução correta!'})

if __name__ == '__main__':
    app.run(debug=True, port=3698) 