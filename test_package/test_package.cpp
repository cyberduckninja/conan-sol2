#include <sol.hpp>

struct S {
    int x;
    int y;
};

int main() {

    sol::state lua;
    S foo{};
    foo.x = 1;
    foo.y = 2;

    lua.open_libraries(sol::lib::base);

    lua.set_function(
            "set_s",
            [&](sol::table table) -> void {
                table["x"] = foo.x;
                table["y"] = foo.y;
            }
    );

    lua.script(
            R"(
            local tmp = {}
            set_s(tmp)
            print(tmp["x"])
            print(tmp["y"])
            )"
    );

    return 0;
}
