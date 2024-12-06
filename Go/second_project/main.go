package main

// go mod init example.com/m
// go get -u github.com/gin-gonic/gin

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func init() {

}

func main() {
	fmt.Println("Second Project started", gin.IsDebugging())
}
