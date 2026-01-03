mkdir -p ~/.streamlit/

# shellcheck disable=SC2028
echo "\
[server]\n\
port = $PORT\n\
enableCORS = true\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
