import { PreventIframe } from "express-msteams-host";

/**
 * Used as place holder for the decorators
 */
@PreventIframe("/yotabssoTab/index.html")
@PreventIframe("/yotabssoTab/config.html")
@PreventIframe("/yotabssoTab/remove.html")
export class YotabssoTab {
}
