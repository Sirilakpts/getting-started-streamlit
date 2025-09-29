import streamlit as st
import graphviz

# --- ตั้งค่าพื้นฐานของหน้าเว็บ ---
st.set_page_config(page_title="แผนเที่ยวบุรีรัมย์", page_icon="🗺️", layout="wide")

st.sidebar.title("เมนูหลัก")
menu_choice = st.sidebar.selectbox(
    "เลือกเมนูที่ต้องการ:",
    ("ข้อมูลแผนเที่ยว", "แบบทดสอบแนะนำแผนเที่ยว")
)

if menu_choice == "ข้อมูลแผนเที่ยว":
    st.title("📌 แนะนำแผนเที่ยวบุรีรัมย์")
    st.write("วางแผนเที่ยวบุรีรัมย์ตามงบประมาณและจำนวนวันที่คุณมี")

elif menu_choice == "แบบทดสอบแนะนำแผนเที่ยว":
    st.title("🗺️ แบบทดสอบแนะนำแผนเที่ยวบุรีรัมย์")
    st.write("เลือกงบประมาณ จำนวนวัน และประเภทกิจกรรม/สถานที่ที่สนใจ")

    # --- รับข้อมูลจากผู้ใช้ ---
    st.sidebar.header("กรอกข้อมูลของคุณที่นี่")
    budget = st.sidebar.radio("1. งบประมาณของคุณ", ["< 1000 บาท", "1000 - 3000 บาท", "> 3000 บาท"])
    duration = st.sidebar.radio("2. จำนวนวันที่เที่ยว", ["1 วัน", "หลายวัน"])
    activity = st.sidebar.radio("3. ประเภทกิจกรรมที่สนใจ", ["ธรรมชาติ/ฟรี", "สถานที่สำคัญ", "กิจกรรมหรู/พิเศษ"])

    if st.sidebar.button("แสดงแผนเที่ยว"):

        # --- สร้างเส้นทางตามตัวเลือกผู้ใช้ ---
        path_nodes = ["Start"]
        path_edges = []
        result = []

        # กำหนดเส้นทางและสถานที่
        if budget == "< 1000 บาท":
            path_nodes.append("งบ <1000")
            path_edges.append(("Start", "งบ <1000"))

            if duration == "1 วัน":
                path_nodes.append("1 วัน")
                path_edges.append(("งบ <1000", "1 วัน"))

                if activity == "ธรรมชาติ/ฟรี":
                    places = ["วนอุทยานเขากระโดง", "พระบรมราชานุสาวรีย์ฯ", "สวนลมบุรีรัมย์"]
                else:
                    places = ["ตลาดชลประทาน", "ลูกชิ้นยืนกินบุรีรัมย์"]

            else:  # หลายวัน
                path_nodes.append("หลายวัน")
                path_edges.append(("งบ <1000", "หลายวัน"))

                if activity == "ธรรมชาติ/ฟรี":
                    places = ["พักแคมป์/โรงแรมราคาประหยัด", "วนอุทยานเขากระโดง", "สวนลมบุรีรัมย์"]
                else:
                    places = ["ตลาดกลางคืน", "ลูกชิ้นยืนกินบุรีรัมย์"]

        elif budget == "1000 - 3000 บาท":
            path_nodes.append("งบ 1000-3000")
            path_edges.append(("Start", "งบ 1000-3000"))

            if duration == "1 วัน":
                path_nodes.append("1 วัน")
                path_edges.append(("งบ 1000-3000", "1 วัน"))

                if activity == "สถานที่สำคัญ":
                    places = ["ปราสาทเขาพนมรุ้ง", "ปราสาทเมืองต่ำ", "สนามช้างอารีน่า"]
                else:
                    places = ["พิพิธภัณฑ์", "คาเฟ่", "แหล่งช้อปปิ้ง"]

            else:  # หลายวัน
                path_nodes.append("หลายวัน")
                path_edges.append(("งบ 1000-3000", "หลายวัน"))

                if activity == "สถานที่สำคัญ":
                    places = ["ปราสาทเขาพนมรุ้ง", "ปราสาทเมืองต่ำ", "สนามช้างอารีน่า", "ศูนย์การเรียนรู้พื้นที่ชุ่มน้ำนกกระเรียนพันธุ์ไทย"]
                else:
                    places = ["พักเกสต์เฮ้าส์ 2-3 ดาว", "คาเฟ่", "ตลาด"]

        else:  # > 3000 บาท
            path_nodes.append("งบ >3000")
            path_edges.append(("Start", "งบ >3000"))

            if duration == "1 วัน":
                path_nodes.append("1 วัน")
                path_edges.append(("งบ >3000", "1 วัน"))

                if activity == "กิจกรรมหรู/พิเศษ":
                    places = ["สนามช้างอารีน่า (ชมการแข่งขัน)", "กิจกรรม Adventure", "ร้านอาหารหรู"]
                else:
                    places = ["ปราสาทเขาพนมรุ้ง", "พิพิธภัณฑ์", "คาเฟ่"]

            else:  # หลายวัน
                path_nodes.append("หลายวัน")
                path_edges.append(("งบ >3000", "หลายวัน"))

                if activity == "กิจกรรมหรู/พิเศษ":
                    places = ["พักโรงแรมหรู/รีสอร์ท", "ปราสาทเขาพนมรุ้ง", "สนามช้างอารีน่า", "ศูนย์การเรียนรู้พื้นที่ชุ่มน้ำนกกระเรียนพันธุ์ไทย"]
                else:
                    places = ["เดินชมเมือง", "พิพิธภัณฑ์", "คาเฟ่", "ตลาดช้อปปิ้ง"]

        # --- เพิ่มโหนดปลายทางแต่ละสถานที่ ---
        for place in places:
            path_nodes.append(place)
            path_edges.append((path_nodes[-2], place))  # เชื่อมจากโหนดก่อนหน้ามายังสถานที่

        # --- สร้างกราฟเฉพาะเส้นทางที่เลือก ---
        dot = graphviz.Digraph(comment='Tourism Decision Tree 4 Layers')
        dot.attr('node', shape='box', style='rounded, filled', fontname='Tahoma', color="#28a745", fillcolor="#d4edda")
        dot.attr('edge', fontname='Tahoma', color="#28a745", penwidth="2.5")

        for node in path_nodes:
            dot.node(node, node)

        for u, v in path_edges:
            dot.edge(u, v)

        # --- แสดงผล ---
        st.header("🌳 แผนภาพการตัดสินใจแผนเที่ยว (4 ชั้นเต็ม):")
        st.graphviz_chart(dot)
        st.success("🏖️ สถานที่ที่แนะนำให้คุณไปเที่ยว:")
        for place in places:
            st.write(f"- {place}")

    else:
        st.info("กรุณาเลือกข้อมูลทางด้านซ้ายและกดปุ่ม 'แสดงแผนเที่ยว' เพื่อเริ่มต้น")
