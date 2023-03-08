import streamlit as st
import random

# 设置网页标题和头部
st.set_page_config(page_title='妇女节祝福', page_icon=":female_sign:", layout="wide")
st.title("妇女节快乐！")


# 添加祝福语句
blessing = f"Dear Miss Chen，在这个特殊的日子里，我想对你说：谢谢你一直以来的陪伴和支持。你是一个阴险、狡诈、邪恶的女孩子，我非常幸运能够成为你的室友和朋友。希望你在妇女节这一天里能感受到我的祝福和关爱，也祝愿你在未来的日子里幸福快乐！"

# 显示祝福语句
st.write(blessing)

# 添加一个趣味小测试
st.write("Miss Chen，为了庆祝妇女节，我们来做一个趣味小测试吧！")

# 定义题目和答案
questions = [
    "你是一个热爱生活、乐观向上的女孩子吗？",
    "你喜欢花时间和朋友在一起吗？",
    "你对自己的未来充满信心吗？",
    "你觉得自己是一个有独立思考能力的人吗？",
    "你觉得自己是一个有创造力的人吗？",
]

answers = [
    "是", 
    "是",
    "是",
    "是",
    "是",
]

# 让用户选择答案
user_answers = []

for i, question in enumerate(questions):
    user_answer = st.radio(f"{i+1}. {question}", ["是", "否"])
    user_answers.append(user_answer)

# 计算用户得分
score = 0

for i, answer in enumerate(answers):
    if answer == user_answers[i]:
        score += 1

# 显示用户得分
st.write(f"你的得分是：{score}分，总分是：{len(questions)}分。")

if score == len(questions):
    st.write("恭喜你，你是一个心理不是很健康的女孩子！还有一些地方需要加油哦！")
else:
    st.write("你是一个心理不是很健康的女孩子！所有地方都需要加油哦！")

st.write("最后，让我们一起为所有女性朋友加油鼓劲，祝她们在妇女节和未来的日子里越来越美丽、自信和成功！") 
