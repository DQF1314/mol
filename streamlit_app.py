import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random
from datetime import datetime, timedelta

def generate_virtual_bazi(start_year=1900, end_year=2023):
    # 随机生成符合历法的虚拟八字
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 简化处理避免闰月问题
    hour = random.randint(0, 23)
    
    # 转换为干支（示例算法片段）
    gan = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    zhi = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    
    # 年柱：以1900年为甲子年推算
    year_gan_idx = (year - 1900) % 10
    year_zhi_idx = (year - 1900) % 12
    year_pillar = gan[year_gan_idx] + zhi[year_zhi_idx]
    
    # 月柱：根据节气简化（假设每月第一个节气）
    month_pillar = gan[(year_gan_idx * 2 + month) % 10] + zhi[(month + 1) % 12]
    
    # 日柱：使用模拟公式（真实需用万年历API）
    day_gan_idx = (year + month + day) % 10
    day_zhi_idx = (month * 2 + day) % 12
    day_pillar = gan[day_gan_idx] + zhi[day_zhi_idx]
    
    # 时柱
    hour_zhi = zhi[hour // 2 % 12]
    hour_gan = gan[(day_gan_idx * 2 + (hour // 2)) % 10]
    hour_pillar = hour_gan + hour_zhi
    
    return {
        'birth_time': f"{year}-{month:02d}-{day:02d} {hour:02d}:00",
        'bazi': f"{year_pillar} {month_pillar} {day_pillar} {hour_pillar}",
        'gender': random.choice(['M', 'F'])
    }
