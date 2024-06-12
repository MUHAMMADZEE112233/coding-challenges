# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Build the React app for production
RUN npm run build

# Serve the React app using serve
RUN npm install -g serve

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run serve to serve the build directory
CMD ["serve", "-s", "build", "-l", "3000"]
