FIND_PATH(LUA_SOURCE_DIR lua.h
	${LUA_SOURCE_ROOT}
	${LUA_SOURCE_ROOT}/src
)
if(LUA_SOURCE_DIR)
	SET(LUA_SOURCE_FOUND TRUE)
else()
	SET(LUA_SOURCE_FOUND FALSE)
endif()