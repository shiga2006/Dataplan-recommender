# 📡 DataPlan Recommender

> *Because your internet plan should be as smart as your phone.*

---

## 🚀 What is This?

Have you ever felt overwhelmed choosing the *“perfect”* internet data plan?  
Too expensive? Not enough data? Too much? Wrong provider?

**DataPlan Recommender** is here to fix that.

This project uses **machine learning** to recommend the best-suited data plans for users based on **who they are** and **how they use the internet**.

---

## 💡 Why I Built This

Most people just pick whatever data plan sounds "okay" — but end up overpaying or running out of data.  
I thought, *"Why not let AI do the thinking?"*  
So I trained models to understand real user habits and make smart recommendations — tailored just for them.

---

## 🧠 How It Works

We collect and process user data like:

- 👤 Age, Occupation, City
- 📱 Device Type (Smartphone, Tablet, TV, etc.)
- 🌐 Preferred Networks (4G/5G, Airtel/VI/BSNL)
- 📊 Daily and Monthly Internet Usage
- 💸 Current Plans and Cost

Our **CatBoost** and **XGBoost** models then predict:

✅ The most suitable plan  
✅ Estimated cost  
✅ Ideal data limit

---

## 🛠️ Tech Stack

| Layer        | Technology Used                   |
|--------------|-----------------------------------|
| 🧠 ML Models  | CatBoost, XGBoost, Scikit-learn   |
| 🐍 Backend   | Flask (Python)                    |
| 🧾 Database  | MongoDB + PyMongo                 |
| 🎨 Frontend  | HTML, CSS, JavaScript, Jinja2     |
| 🔗 API       | Flask Routes with JSON Handling   |

---

## 🔍 Dataset Overview

The dataset contains realistic telecom-related info:

- Name, Age, Mobile Number
- Occupation (e.g., Doctor, Teacher, IT)
- Location (City)
- Internet usage in MB/GB (daily & monthly)
- Network Preference and Device Type
- Package details: Data limit, Network, Cost

Goal? Understand usage patterns and suggest smarter data plans.

---

## 🧪 Methodology (in simple words)

1. 📥 **Collect Data** – Gather user info + usage history  
2. 🧼 **Clean It Up** – Remove noise, convert units, encode values  
3. 📊 **Train Models** – Use CatBoost & XGBoost to find the best fit  
4. 🧪 **Test & Tune** – Optimize for accuracy and reliability  
5. 🖥 **Frontend Fun** – Let users interact and see their results  
6. ☁️ **Save in MongoDB** – Store user info securely

---

## 📈 Results

Here’s what we achieved:

- 🧠 **Smart Predictions** – High accuracy in finding the right data plan
- 💡 **User-Focused UX** – Simple and clear plan suggestions
- 💰 **Cost Savings** – Balanced usage vs. cost = happy users
- 📊 **Network Insights** – Providers can learn from trends too

---

## 📸 Sneak Peek (Screenshots)

> A glimpse of the system in action:

![1](https://github.com/user-attachments/assets/c50de068-9c07-4fc5-9acd-77e1807619fc)  
![2](https://github.com/user-attachments/assets/4f639b44-43c7-49de-9f2d-53f761b45b7c)  
![3](https://github.com/user-attachments/assets/45597dbf-c6dd-4d0a-bf60-aa204a5376fd)  
![4](https://github.com/user-attachments/assets/4a22a2db-3909-47ac-bc83-b179644215ab)  
![5](https://github.com/user-attachments/assets/fe502958-ec46-4999-af18-79653188fd0d)  
![6](https://github.com/user-attachments/assets/ae72c66a-68f2-4665-843a-2a2aff64ecf8)  
![7](https://github.com/user-attachments/assets/3aa55c1e-fb75-4d74-9acd-3c8ed19ea849)

---

## 🎬 Demo Video

Watch the full walk-through here:  
📽️ [Click to View Demo](https://github.com/user-attachments/assets/8b548f92-49d6-45ab-bdd1-735223db33c7)

---

## 🧩 Future Upgrades

- [ ] Real-time API integration with telecom providers
- [ ] Add SMS/email-based plan recommendations
- [ ] User login & history-based suggestions
- [ ] Mobile app version (React Native/Flutter)

---

## 🤝 Contributions & Feedback

Got ideas to improve this project? Found a bug? Want to collaborate?

Open an issue, create a pull request, or just connect with me!

---

## 🔗 Let’s Connect

Drop your thoughts or questions — always open for collaboration!  
Don’t forget to ⭐ this repo if you found it interesting!

---

> "Build systems that *think* for the user — not make the user think."

