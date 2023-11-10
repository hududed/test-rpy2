import streamlit as st
import rpy2.robjects as ro


def main():
    ro.r(
        """
        print_hello_world <- function() {
            return("Hello World!")
        }
    """
    )
    with ro.default_converter.context():
        result = ro.r["print_hello_world"]()
        r_data = ro.conversion.get_conversion().rpy2py(result)
    st.write(r_data)


if __name__ == "__main__":
    main()
