package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

type album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

var albums = []album{
	{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
	{ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

func getAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, albums)
}

// postAlbums adds an album from JSON received in the request body.
func postAlbums(c *gin.Context) {
	var newAlbum album // Create a variable of type album

	// Call BindJSON to bind the received JSON to
	// newAlbum. => Binds the passed struct pointer(newAlbum) to the received JSON
	if err := c.BindJSON(&newAlbum); err != nil {
		return
	}
	// Add the new album to the slice.
	albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusCreated, newAlbum)
}

func getOneAlbum(c *gin.Context) {
	id := c.Param("id")
	fmt.Println(c.Accepted, c.Errors, c.Keys, c.Params)
	if c.Request.Method == "GET" {
		for _, album := range albums {
			if id == album.ID {
				c.IndentedJSON(http.StatusOK, album)
				return
			}
		}
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "No Album Found"})
	} else if c.Request.Method == "PUT" {
		fmt.Println(c.Request.Body)
		c.IndentedJSON(http.StatusAccepted, "PUT")
	}
}

func updateAlbum(c *gin.Context) {
	id := c.Param("id")
	fmt.Println(c.Keys, id)
	c.IndentedJSON(http.StatusAccepted, gin.H{"message": "update"})
}

// c.AddParam("id", "2")
// fmt.Println(c.ClientIP())
// fmt.Println(c.Request.Method, id)
