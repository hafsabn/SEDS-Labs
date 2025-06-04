const baseURL = "http://127.0.0.1:8000"; // Replace with your FastAPI server URL

// Show All Users
document.getElementById("getAllUsers").addEventListener("click", async () => {
    const response = await fetch(`${baseURL}/users/`);
    const users = await response.json();
    const usersList = document.getElementById("usersList");
    usersList.innerHTML = ""; // Clear previous data
    users.forEach(user => {
        const li = document.createElement("li");
        li.textContent = `${user.id}: ${user.name} (${user.email})`;
        usersList.appendChild(li);
    });
});

// Show User By ID
document.getElementById("getUserById").addEventListener("click", async () => {
    const userId = document.getElementById("userIdInput").value;
    const response = await fetch(`${baseURL}/users/${userId}`);
    const user = await response.json();
    const userDetails = document.getElementById("userDetails");
    if (response.ok) {
        userDetails.textContent = `ID: ${user.id}, Name: ${user.name}, Email: ${user.email}`;
    } else {
        userDetails.textContent = user.detail; // Error message from FastAPI
    }
});

// Create New User
document.getElementById("createUser").addEventListener("click", async () => {
    const name = document.getElementById("userName").value;
    const email = document.getElementById("userEmail").value;
    const response = await fetch(`${baseURL}/users/new`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email })
    });
    const result = await response.json();
    document.getElementById("createUserResponse").textContent = response.ok
        ? `User created: ID ${result.id}, Name ${result.name}`
        : result.detail; // Error message
});

// Create New Post
document.getElementById("createPost").addEventListener("click", async () => {
    const userId = document.getElementById("postUserId").value;
    const title = document.getElementById("postTitle").value;
    const content = document.getElementById("postContent").value;
    let publishedAt = new Date().toISOString();  // This will generate a timestamp in ISO 8601 format
    

    // Send the data to the server
    const response = await fetch(`${baseURL}/users/${userId}/posts/new`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ publishedAt, title, content })
    });

    // Handle the response
    const result = await response.json();
    document.getElementById("createPostResponse").textContent = response.ok
        ? `Post created: ID ${result.id}, Title ${result.title}`
        : result.detail; // Error message
});


// Show Posts of a User
document.getElementById("getUserPosts").addEventListener("click", async () => {
    const userId = document.getElementById("postsUserId").value;
    const response = await fetch(`${baseURL}/users/${userId}/posts/`);
    const posts = await response.json();
    const postsList = document.getElementById("postsList");
    postsList.innerHTML = ""; // Clear previous data
    posts.forEach(post => {
        const li = document.createElement("li");
        li.textContent = `Post ID: ${post.id}, Title: ${post.title}`;
        postsList.appendChild(li);
    });
});

// Delete Post
document.getElementById("deletePost").addEventListener("click", async () => {
    const userId = document.getElementById("deleteUserId").value;
    const postId = document.getElementById("deletePostId").value;
    const response = await fetch(`${baseURL}/users/${userId}/delete_post/${postId}`, {
        method: "DELETE",
    });
    document.getElementById("deletePostResponse").textContent = response.ok
        ? "Post successfully deleted"
        : "Failed to delete post"; // Error message
});
