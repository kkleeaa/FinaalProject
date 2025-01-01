import streamlit as st

def manage_financial_goals(db):
    st.subheader("Set and Track Your Financial Goals")

    with st.expander("Set a New Goal"):
        goal_name= st.text_input("Goal Name")
        target_amount= st.number_input("Target Amount", min_value=0.0, format="%.2f")
        if st.button("Add Goal"):
            db.add_goal(goal_name, target_amount)
            st.success("Goal added successfully!")
    st.subheader("Current Goals")
    goals= db.get_goals()
    for goal in goals:
        goal_id, name, target, saved= goal
        st.write(f"**{name}**: ${saved:.2f} saved out of ${target:.2f}")
        if saved< target:
            add_amount= st.number_input(f"Add to {name}", min_value= 0.0, format="%.2f", key= f"goal_{goal_id}")
            if st.button(f"Update {name}",key= f"Update {goal_id}"):
                db.update_goal(goal_id, add_amount)
                st.success(f"Updated savings fpr {name}!")

