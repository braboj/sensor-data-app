# Use the official Node.js image as the base image
FROM node:alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install angular-cli globally
RUN npm install -g @angular/cli

// Install the dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the application will run on
EXPOSE 4200

# Start the application in development mode
CMD ["ng", "serve", "--host", "0.0.0.0"]