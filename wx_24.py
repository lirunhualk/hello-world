import itertools
from itertools import combinations_with_replacement

def generate_24_problems():
    """生成所有可能的24点题目（数字1-13）"""
    problems = []
    
    # 生成所有可能的4个数字组合（允许重复）
    for combo in combinations_with_replacement(range(1, 14), 4):
        # 生成该组合的所有排列
        for perm in set(itertools.permutations(combo)):
            problems.append(list(perm))
    
    return problems

def write_problems_to_file(problems, filename="24_problems.txt"):
    """将题目写入文本文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"24点游戏题目集合（共{len(problems)}道题）\n")
        f.write("="*50 + "\n\n")
        
        for i, problem in enumerate(problems, 1):
            f.write(f"{i:5d}. {problem[0]:2d} {problem[1]:2d} {problem[2]:2d} {problem[3]:2d}\n")
    
    print(f"已生成 {len(problems)} 道24点题目，保存到 {filename}")

if __name__ == "__main__":
    # 生成所有24点题目
    all_problems = generate_24_problems()
    
    # 写入文件
    write_problems_to_file(all_problems)