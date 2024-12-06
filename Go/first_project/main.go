package main

import (
	"github.com/gin-gonic/gin"
)

/*
like a request object inside view: gin.Context is the most important part of Gin. It carries request details, validates and serializes JSON, and more.
Serializer: Call Context.IndentedJSON to serialize the struct into JSON and add it to the response.
Server to up and run: Use the Run function to attach the router to an http.Server and start the server.
*/

// Format: router.GET("path", func(...) {})
func main() {
	router := gin.Default()
	router.GET("/albums", getAlbums)
	router.POST("/albums", postAlbums)
	router.GET("/albums/:id", getOneAlbum)
	router.Run("localhost:9000") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
