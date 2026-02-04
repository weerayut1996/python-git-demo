import numpy as np
from scipy.optimize import minimize
# 1. นิยาม "แรงดึง" ทางกฎหมาย (เหมือนกฎของ Hooke: F = kx)


def legal_energy_function(fine_amount, min_limit, max_limit, damage_caused):
    # fine_amount คือตัวแปรที่ AI ต้องหา (เหมือนตำแหน่งของวัตถุ)
    # พลังงานจากแรงดึงของกฎหมายขั้นต่ำ (ถ้าต่ำกว่าเกณฑ์ พลังงานจะสูงขึ้นมาก)
    penalty_min = 100 * max(0, min_limit - fine_amount)**2
    # พลังงานจากแรงดึงของกฎหมายขั้นสูง (ถ้าสูงกว่าเกณฑ์ พลังงานจะสูงขึ้นมาก)
    penalty_max = 100 * max(0, fine_amount - max_limit)**2
    # พลังงานจากความเสียหายจริง (AI พยายามให้ค่าปรับใกล้เคียงความเสียหาย)
    penalty_damage = (fine_amount - damage_caused)**2
    # พลังงานรวม (Total Potential Energy)
    return penalty_min + penalty_max + penalty_damage


# 2. ตั้งค่าสถานการณ์ (Case Study)
case_min_law = 500      # กฎหมายบอกต้องปรับอย่างน้อย 500
case_max_law = 2000     # กฎหมายบอกปรับได้ไม่เกิน 2000
case_damage = 1200      # ความเสียหายที่เกิดขึ้นจริงในคดีนี้คือ 1200
# 3. ให้ AI ประมวลผลหาจุดสมดุล (Optimization)
initial_guess = (case_min_law + case_max_law) / 2
result = minimize(legal_energy_function, initial_guess,
                  args=(case_min_law, case_max_law, case_damage))
# 4. แสดงผลลัพธ์
optimized_fine = result.x[0]
print(f"--- ผลการคำนวณจาก Physics-Informed AI ---")
print(f"จุดสมดุลของค่าปรับที่เหมาะสมที่สุด: {optimized_fine:.2f} บาท")
