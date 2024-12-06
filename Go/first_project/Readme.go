package main

/*

Anology:
Gin is a package that consists of contants, variables, functions, composite types like Maps, Structs like Context and so on...

Constants
Format of the GIN-DEBUG:
	var DebugPrintRouteFunc func(httpMethod, absolutePath, handlerName string, nuHandlers int)
var DefaultErrorWriter io.Writer = os.Stderr // helps to display error messages on the terminal
var DefaultWriter io.Writer = os.Stdout  // helps to display debug messages on the terminal

Functions
Returns fresh engine or context for testing purposes:
	func ContextTestCreate(w http.ResponseWriter) (c *Context, r *Engine)

Modes Available: gin.DebugMode; gin.ReleaseMode; gin.TestMode
Mode Functions: func IsDebugging() bool; func SetMode(gin.ReleaseMode); func Mode() string;
These functions can be accessed by gin.IsDebugging() and so on...

c *gin.Context
--------------
Context: Request, Writer ResponseWriter, Keys, Params, Accepted, Errors

c.AddParam(key, value string) => Used while e2e testing, as it maipulates gin.Context.Params
c.Cookie(name string); c.ContentType() string;
c.Copy() returns the current context that can be used safely outside the given scope;
c.FullPath()
c.GetHeader(key string) => returns value from request header

c.GetPostForm(key string) => returns the specified key from POST urlencoded
c.GetPostFormArray(key string); c.GetPostFormMap(key string);

c.GetQuery() or c.Query()
c.GetQuery(key) (string, bool) => returns value from Query parameters; c.Request.URL.Query.Get(key)
c.GetQueryArray(key) ([]string, bool); c.GetQueryMap(key string) (map[string]string, bool)

c.MultipartForm() => including file uploads

c.SetCookie(); c.SetSameSite()

c.Status()

Content-types:
c.AsciiJSON(status int, obj any) => serializes struct type as JSON into response body
c.BindJSON(obj any) => Binds the passed struct pointer to the received JSON
c.BINDYAML(), c.BINDXML() ...

type IRouter interface {
	IRoutes
	Group(string, ...HandlerFunc) *RouterGroup

type LogFormatterParams struct {
	TimeStamp, StatusCode, ClientIP, Latency, Method, Path, ErrorMessage, BodySize
}

}

*/
