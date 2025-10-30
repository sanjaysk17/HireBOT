# ⚛️ Frontend Dockerfile

# 1️⃣ Use Node.js official image
FROM node:18

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# 4️⃣ Copy remaining frontend files
COPY . .

# 5️⃣ Expose port for React app
EXPOSE 3000

# 6️⃣ Start the app
CMD ["npm", "start"]
