FROM node:18

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy project files
COPY . .

# Expose the port
EXPOSE 3000

# Start development server
CMD ["npm", "run", "dev"]
